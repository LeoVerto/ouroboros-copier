import re
import os
import pathlib
import json

from dataclasses import dataclass, asdict


@dataclass(unsafe_hash=True)
class Circle:
    label: str = ""
    key: str = ""
    joined: bool = False
    betrayed: bool = False

    def __post_init__(self):
        self.label = self.label.lower()
        self.key = self.key.lower()

    def equal(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.label, self.key) == (other.label, other.key)

    @property
    def __dict__(self):
        return asdict(self)


def load_command_file(file):
    circles = set()
    regex = re.compile(r"label:(.*)\s+key:(.*)")
    with open(file, "r") as f:
        for line in f:
            m = regex.search(line)
            if m:
                circles.add(Circle(m.group(1), m.group(2)))
    return circles


def load_key_file(file):
    circles = set()
    regex = re.compile(r"\((.*)\)\s+\((.*)\)")
    with open(file, "r") as f:
        for line in f:
            m = regex.match(line)
            if m:
                circles.add(Circle(m.group(1), m.group(2)))
    return circles


def load_joined_labels():
    labels = []
    with open("circles/joined.txt") as f:
        for line in f:
            labels.append(line.lower().strip())
    return labels


def get_duplicate_labels(circles):
    labels = []
    dupes = []
    for circle in circles:
        if circle.label in labels:
            dupes.append(circle.label)
        else:
            labels.append(circle.label)
    return dupes


def set_joined(circles):
    joined = load_joined_labels()
    for circle in circles:
        if circle.label in joined:
            circle.joined = True
    return circles


def get_unjoined(circles):
    unjoined = []
    for circle in circles:
        if not circle.joined:
            unjoined.append(circle)
    return unjoined


def write_circles(circles):
    circle_dicts = [c.__dict__ for c in circles]

    with open("circles/circles.json", "w") as f:
        f.write(json.dumps(circle_dicts, indent=2))


def load_and_get_unjoined_circles():
    circles = set()
    for path in pathlib.Path("./circles").glob("*_commands.txt"):
        circles |= load_command_file(path)

    for path in pathlib.Path("./circles").glob("*_keys.txt"):
        circles |= load_key_file(path)

    circles = set_joined(circles)

    print(f"Loaded {len(circles)} unique circles.")
    write_circles(circles)
    unjoined = get_unjoined(circles)
    print(f"Found {len(unjoined)} unjoined circles.")
    # print(unjoined)
    return unjoined


if __name__ == "__main__":
    load_and_get_unjoined_circles()
