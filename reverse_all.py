#!/usr/bin/env python

import os
import sys
import struct
import json


class Header:
    def __init__(self, crc, root_obj_table_size):
        self._crc = crc
        self._root_obj_table_size = root_obj_table_size

    @property
    def crc(self):
        return self._crc

    @property
    def root_obj_table_size(self):
        return self._root_obj_table_size


class ObjectTableEntry:
    BYTE_SIZE = 16

    def __init__(self, hash1, hash2, obj_type, obj_offset):
        self._hash1 = hash1
        self._hash2 = hash2
        self._obj_type = obj_type
        self._obj_offset = obj_offset

    @property
    def hash1(self):
        return self._hash1

    @property
    def hash2(self):
        return self._hash2

    @property
    def type(self):
        return self._obj_type

    @property
    def offset(self):
        return self._obj_offset


class Value:
    def __init__(self, hash1, hash2, value):
        self.hash1 = hash1
        self.hash2 = hash2
        self.value = value


class Object:
    counter = 0

    def __init__(self, hash1, hash2, data, offset, object_table_entries,
                 parent, is_list):
        self.id = Object.counter
        Object.counter += 1

        self.hash1 = hash1
        self.hash2 = hash2
        self.data = data
        self.offset = offset
        self.object_table_entries = object_table_entries
        self.childs_begin = offset + len(
            object_table_entries) * ObjectTableEntry.BYTE_SIZE
        self.childrens = []
        self.parent = parent
        self.is_list = is_list

    def populate_childrens(self):
        data = self.data
        print(
            f"Pop childs of {self.id} child of {self.parent.id if self.parent else 'none'}"
        )
        for entry in self.object_table_entries:
            print(
                f"Checking entry(type={entry.type}) defining object offset={self.childs_begin + entry.offset:02x}: ",
                end="")
            if entry.type == 0:
                ptr = self.childs_begin + entry.offset
                value, = struct.unpack('f', data[ptr:ptr + 4])
                print(f"Value is float {value}")
                self.childrens.append(Value(entry.hash1, entry.hash2, value))
            elif entry.type == 1:
                ptr = self.childs_begin + entry.offset
                val_int = int.from_bytes(data[ptr:ptr + 4],
                                         byteorder='little',
                                         signed=True)
                self.childrens.append(Value(entry.hash1, entry.hash2, val_int))
                print(f"Value is int {val_int}")
            elif entry.type == 2:
                ptr = self.childs_begin + entry.offset
                val_int = int.from_bytes(data[ptr:ptr + 1], byteorder='little')
                self.childrens.append(Value(entry.hash1, entry.hash2, val_int))
                print(f"Value is uint8 {val_int}")
            elif entry.type == 3:
                ptr = self.childs_begin + entry.offset
                start_ptr = ptr
                while self.data[ptr] != 0:
                    ptr += 1
                value = self.data[start_ptr:ptr].decode('ascii')
                self.childrens.append(Value(entry.hash1, entry.hash2, value))
                print(f"Value is str {value}")
            elif entry.type == 4:
                print("4 not handled")
            elif entry.type == 100 or entry.type == 101:
                obj = Object.make(self.data,
                                  self.childs_begin + entry.offset,
                                  parent=self,
                                  entry_hash1=entry.hash1,
                                  entry_hash2=entry.hash2,
                                  is_list=entry.type == 101)
                self.childrens.append(obj)
            #elif entry.type == 101:
            #    print("101 not handled")
            else:
                print(f"{entry.type} UNEXPECTED")

    @classmethod
    def make(cls,
             data,
             offset,
             num_entries=None,
             parent=None,
             entry_hash1=0,
             entry_hash2=0,
             is_list=False):
        print(f"Building object at offset={offset:02x}")
        if num_entries == None:
            num_entries = int.from_bytes(data[offset:offset + 4],
                                         byteorder='little')
            offset += 4

        object_table_entries = []
        end = offset + num_entries * ObjectTableEntry.BYTE_SIZE
        for ptr in range(offset, end, ObjectTableEntry.BYTE_SIZE):
            hash1 = int.from_bytes(data[ptr:ptr + 4], byteorder='little')
            hash2 = int.from_bytes(data[ptr + 4:ptr + 8], byteorder='little')
            obj_type = int.from_bytes(data[ptr + 8:ptr + 12],
                                      byteorder='little')
            obj_offset = int.from_bytes(data[ptr + 12:ptr + 16],
                                        byteorder='little')
            entry = ObjectTableEntry(hash1, hash2, obj_type, obj_offset)
            object_table_entries.append(entry)
            print(f"\tBuild entry(type={obj_type}) read at ptr={ptr:02x}")

        return cls(entry_hash1, entry_hash2, data, offset,
                   object_table_entries, parent, is_list)


class RGDFile:
    def __init__(self, data):
        self._data = data
        self.header = None
        self.root_obj_table = []
        self.root = None

    def parse(self):
        data = self._data
        crc = int.from_bytes(data[0:4], byteorder='little')
        size = int.from_bytes(data[4:8], byteorder='little')
        header = Header(crc, size)

        print(
            f"root_obj_table_size={header.root_obj_table_size}, crc={header.crc}"
        )

        self.root = Object.make(data,
                                8,
                                num_entries=header.root_obj_table_size)

        self.root.populate_childrens()
        t100_childs = list(
            filter(lambda c: isinstance(c, Object), self.root.childrens))

        print("==Start BFS==")
        while len(t100_childs) != 0:
            obj = t100_childs.pop()
            print(
                f"Parse objtableentry={len(obj.object_table_entries)} offset={obj.offset:02x}"
            )

            obj.populate_childrens()
            new_t100s = list(
                filter(lambda c: isinstance(c, Object), obj.childrens))
            print(f"Found {len(new_t100s)} new t100 obj\n")
            t100_childs += new_t100s


class Key:
    def __init__(self, hash1, hash2, value):
        self.hash1 = hash1
        self.hash2 = hash2
        self.value = value


def parse_key(data, ptr):
    hash1 = int.from_bytes(data[ptr:ptr + 4], byteorder='little', signed=False)
    hash2 = int.from_bytes(data[ptr + 4:ptr + 8],
                           byteorder='little',
                           signed=False)
    str_width = int.from_bytes(data[ptr + 8:ptr + 12],
                               byteorder='little',
                               signed=False)

    #print(f"hash1={hash1}, hash2={hash2}, width={str_width}")

    value = data[ptr + 12:ptr + 12 + str_width].decode('ascii')
    return (12 + str_width, Key(hash1, hash2, value))


def parse_keys(infile):
    with open(infile, 'rb') as f:
        data = f.read()

    ptr = 4
    keys = {}
    while ptr < len(data):
        offset, key = parse_key(data, ptr)

        if key.hash1 in keys or key.hash2 in keys:
            print("May not work.............")

        keys[key.hash1] = key
        keys[key.hash2] = key
        ptr += offset

    return keys


def parse_aegd(infile, keys):
    with open(infile, 'rb') as f:
        data = f.read()

    rgd = RGDFile(data)
    rgd.parse()
    return rgd


def produce_output(rgd, keys):
    def recurse(obj, keys, output):
        if not obj.is_list:
            for c in obj.childrens:
                if c.hash1 not in keys or c.hash2 not in keys:
                    print("{c.hash1} NOT in there")
                else:
                    key = keys[c.hash1].value

                if isinstance(c, Object):
                        nested_output = {}
                        recurse(c, keys, nested_output)
                        output[key] = nested_output
                else:
                    output[key] = c.value
        else:
            items = []
            for c in obj.childrens:
                if c.hash1 not in keys or c.hash2 not in keys:
                    print("{c.hash1} NOT in there")
                else:
                    key = keys[c.hash1].value

                if isinstance(c, Object):
                    nested_output = {}
                    recurse(c, keys, nested_output)
                    items.append({key: nested_output})
                else:
                    items.append({key: c.value})
            output['list'] = items


    output = {}
    recurse(rgd.root, keys, output)
    return output

def get_folders(path):
    print(":: Reading folders")
    list_of_files = []
    for root,d_names,f_names in os.walk(path):
        if ('AEGD-Chunk-0.bin' in f_names or 'AEGD-Chunk-0.meta' in f_names or 'KEYS-Chunk-1.bin' in f_names or 'KEYS-Chunk-1.meta' in f_names):
            list_of_files.append(root)
    return list_of_files


if len(sys.argv) != 2:
    print("first arg data dir")
    sys.exit(1)

path = sys.argv[1]

data_dirs = get_folders(path)

for data_dir in data_dirs:
    print(f":: Processing {data_dir}...")
    try:
        keys_file = f"{data_dir}/KEYS-Chunk-1.bin"
        aegd_file = f"{data_dir}/AEGD-Chunk-0.bin"

        if not os.path.exists(keys_file):
            print(f"{keys_file} doesn't exists")
            sys.exit(1)

        if not os.path.exists(aegd_file):
            print(f"{aegd_file} doesn't exists")
            sys.exit(1)

        keys = parse_keys(keys_file)
        rgd = parse_aegd(aegd_file, keys)

        outfile = f"{data_dir}.json"

        output = produce_output(rgd, keys)

        print(f"Writing to {outfile}", file=sys.stderr)
        with open(outfile, 'w') as f:
            f.write(json.dumps(output, indent=2))
            #print(json.dumps(output, indent=2))
        print(f":: {data_dir} Processed")
    except:
        print(f":: Error processing {data_dir}")
