#!/usr/bin/env python

import os
import glob
import shutil

def clean_recent():
    flist = glob.glob("----/Assets/Resources/Licenses/*")

    for f in flist:
        os.remove(f)


def generate_source_file(framelist):
    src = """//
//  OSS.generated.swift
//
//  DO NET EDIT THIS FILE MANUALLY
//

import Foundation

enum OpenSourceLibraries {
    static let libraries: [String] = [
"""

    for frame in framelist:
        src += "        \"" + frame + "\",\n"

    src += """
    ]
}
"""
    path_w = "----/OSS.generated.swift"


    with open(path_w, mode='w') as f:
        f.write(src)


if __name__ == "__main__":
    print("Searching Carthage built frameworks...")
    clean_recent()
    framelist = os.listdir("Carthage/Checkouts/")

    licensed_frames = framelist

    for i, frame in enumerate(framelist):
        print("Processing for " + frame + " ...")
        if os.path.isfile("./Carthage/Checkouts/" + frame + "/LICENSE"):
            shutil.copyfile("./Carthage/Checkouts/" + frame + "/LICENSE", "./----/Assets/Resources/Licenses/" + frame + ".license")
            continue

        if os.path.isfile("./Carthage/Checkouts/" + frame + "/LICENSE.txt"):
            shutil.copyfile("./Carthage/Checkouts/" + frame + "/LICENSE.txt", "./----/Assets/Resources/Licenses/" + frame + ".license")
            continue

        if os.path.isfile("./Carthage/Checkouts/" + frame + "/LICENSE.md"):
            shutil.copyfile("./Carthage/Checkouts/" + frame + "/LICENSE.md", "./----/Assets/Resources/Licenses/" + frame + ".license")
            continue

        licensed_frames.pop(i)

    generate_source_file(licensed_frames)
