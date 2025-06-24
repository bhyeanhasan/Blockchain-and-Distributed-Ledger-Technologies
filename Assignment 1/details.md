ICT 6106: Blockchain and Distributed Ledger Technologies

Assignment 1

22/06/2025

Total Mark: 10

Due: 25/07/2025

Comparative study of Different Hashing Algorithms

1. Implement the following hashing algorithms. Use existing library from Java, Python, etc.,
for implementation.
i. MD5
ii. SHA-1
iii. SHA-2 (256 bit)
iv. SHA-2 (512 bit)
v. SHA-3 (256 bit)
vi. SHA-3 (512 bit)
2. Download 3 text files from https://examplefile.com/
i. 1 GB
ii. 500 MB
iii. 100 MB
3. Using your program, generate hash values for the 3 files for each of the algorithms with
prefix 000XYZ, where XXX = Last 3 digits of your student ID.
4. Identify running time for each input file for the selected algorithms
5. Prepare a report with
1. Details of the library used for analysis
2. Screenshots of the outputs
3. Computer spec
4. Hash values
5. Comparative analysis
6. Submit the report in Teams in PDF format.

PLAGIARISM SOFTWARE WILL BE USED FOR DETECTION. ALL MATCHING
SUBMISSIONS WILL GET ZERO. 


### Output

```
File:  ../data/100mb.txt
MD5 -> Hash: 0000016961c040063fac02ee015dcec60f4392 || Time: 0.1552s
SHA-1 -> Hash: 0000011f59e7fc2100422c06b99cd53c376e2a04ed0ac6 || Time: 0.0416s
SHA-256 -> Hash: 000001e842bc146b244ac5ac96afff5d32a9e1f27690ef7168fa11c84d09e5c39fd270 || Time: 0.0429s
SHA-512 -> Hash: 000001df587105f1d3c05ff9350979f9d88c260603c3ea4432ad11ea479b01ad520c88d190b87a981a8c513a9dd11ff7e0fa4973c423ef0fbc4c8bceaa848e6b754a89 || Time: 0.0693s
SHA3-256 -> Hash: 000001687686085f14fadb9b4314b2acbfe7165844ae44af6f97f0d8e912f514403989 || Time: 0.1075s
SHA3-512 -> Hash: 000001dde55c5e2c7dcee6eaea3c186780f041f7f1fbb00e505db2dd4b99bcc9e1f3e960ac8edde1984906ed3064cc4111f4521a273b84160972ad8c6c0b62ba18eafe || Time: 0.1918s


File:  ../data/500mb.txt
MD5 -> Hash: 00000122672abacc658f10ca511b877941baff || Time: 0.8911s
SHA-1 -> Hash: 0000011f4e25d4c6ea1f1dd915b1394047eeb9d36dd91d || Time: 0.2333s
SHA-256 -> Hash: 000001711597cadcc93066c17e0825a92f12815197ccc9732c84ff92a34f732233ab13 || Time: 0.2210s
SHA-512 -> Hash: 0000012f276d00ea2da39cd88c77aa23b1fb12f11211fd0ebc62b54fda0d09ce08ccfc167a581618963da6cdfd43286a34cf9465bc67b16986ec2c09050c0a6b3c9497 || Time: 0.3432s
SHA3-256 -> Hash: 0000012eac554514e3ee404528cd58ea21b3ce461a10ca5a6ca937d1c62c32abe28257 || Time: 0.5427s
SHA3-512 -> Hash: 000001e24d61311584b67bb507abff9399429fb400bc672db4880bcbe08e28743edf8dc755c3a5e1a55ca38ceab09f400b636eae16161a680f36d53061838295775262 || Time: 0.9527s


File:  ../data/1000mb.txt
MD5 -> Hash: 000001b7cbf4b58d33c0a325617386e9e69ace || Time: 1.7129s
SHA-1 -> Hash: 0000019e49ede4843795d3760f431e44fa60a74d8e950e || Time: 0.4203s
SHA-256 -> Hash: 0000012bf32157d40c7233d3ccb26035d6389cd1c559090a8ae1a3aabc971af4b6e1c1 || Time: 0.4802s
SHA-512 -> Hash: 000001ef8d54365424ef6c5000bf0ea33a2ef06757a7a026d0042020c1093ef2d5dfd19946507b82853195a1261f1cfa9474e2a799cdcf6a96d9b3afe4a4aa138b9f13 || Time: 0.6967s
SHA3-256 -> Hash: 000001d497dca0edfddd112d6512f213a06af15f57bceb44d116d544c05af461f91d8f || Time: 1.0952s
SHA3-512 -> Hash: 000001583b7bdf3f1afdde1029901c45636b292eb5aa85b84c7104f97fc1d96191db96ce66f90b7f2aee9adefe167cfd218367abd2ad8a3af168811163f3c930ed5db2 || Time: 1.9802s
```

### Screenshot

![Alt text](Screenshot.png)