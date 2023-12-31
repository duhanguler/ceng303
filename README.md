# Welcome to our CENG303 Project!

Hi! Our project is **ProjectX**. 



## 🎯 Features

OMR checking software that can read and evaluate OMR sheets scanned at any angle and having any color. Independent for scanner or mobile camera. Just you need image!

| Specs <img width=200/> | ![Current_Speed](https://img.shields.io/badge/Speed-220+_OMRs/min-blue.svg?style=flat-square) ![Min Resolution](https://img.shields.io/badge/Min_Resolution-640x480-blue.svg?style=flat-square) <img width=200/> |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 💯 **Accurate**        | Currently nearly 100% accurate on good quality document scans; and about 95% accurate on mobile images.                                                                                                          |
| 💪🏿 **Robust**          | Supports low resolution  with Robust feature.                                                                                                                                                                    |
| ⏩ **Fast**            | Current processing speed without any optimization is 220 OMRs/minute.                                                                                                                                            |
| ✅ **Customizable**    | Easily custom  OMR layouts.                                                                                                                                                                                      |
| 📊 **Visually Rich**   | Visually rich console using.                                                                                                                                                                                     |
| 🎈 **Lightweight**     | Very minimal and lightweight core code.                                                                                                                                                                          |
| 🏫 **Large Scale**     | Tested with [Nokta Tek Egitim Kurumlari](https://noktatek.com.tr) and Cozum Yenimahalle exams.                                                                                                                   |

# Contributors

- [duhanguler](https://github.com/duhanguler)
- [elffbykll](https://github.com/elffbykll)
- [erayerglc](https://github.com/erayerglc)

You can contribute our project with TODO sections.
For example ![To_Do](https://i.imgur.com/clNhDCM.png)

## Getting started

![Setup Time](https://img.shields.io/badge/Setup_Time-10_min-blue.svg)

**Operating system:** OSX or Linux is recommended although Windows is also supported.

### 1. Install global dependencies

![opencv 4.0.0](https://img.shields.io/badge/opencv-4.0.0-blue.svg) ![python 3.5+](https://img.shields.io/badge/python-3.7+-blue.svg)

To check if python3 and pip is already installed:

```bash
python3 --version
python3 -m pip --version
```

<details>
	<summary><b>Install Python3</b></summary>

To install python3 follow instructions [here](https://www.python.org/downloads/)

To install pip - follow instructions [here](https://pip.pypa.io/en/stable/installation/)

</details>
<details>
<summary><b>Install OpenCV</b></summary>

**Any installation method is fine.**

Recommended:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user opencv-python
python3 -m pip install --user opencv-contrib-python
```

More details on pip install openCV [here](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/).

</details>

<details>

<summary><b>Extra steps(for Linux users only)</b></summary>

<b>Installing missing libraries(if any):</b>

On a fresh computer, some of the libraries may get missing in event after a successful pip install. Install them using following commands[(ref)](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/):

```bash
sudo apt-get install -y build-essential cmake unzip pkg-config
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libatlas-base-dev gfortran
```

</details>

### 2. Install project dependencies

Clone the repo

```bash
git clone https://github.com/duhanguler/omr
cd omr/
```

Install pip requirements

```bash
python3 -m pip install --user -r requirements.txt
```

_**Note:** If you face a distutils error in pip, use `--ignore-installed` flag in above command._

<!-- Wiki should not get cloned -->

### 3. Run the code

1. First copy and examine the sample data to know how to structure your inputs:
   ```bash
   cp -r ./samples/sample1 inputs/
   # Note: you may remove previous inputs (if any) with `mv inputs/* ~/.trash`
   # Change the number N in sampleN to see more examples
   ```
2. Run program:
   ```bash
   python3 main.py
   ```

Alternatively you can also use `python3 main.py -i ./samples/sample1`.

Each example in the samples folder demonstrates different ways in which OMR can be used.

## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram

  M ->> RC: create()
  M ->> RC: shuffle()
  M ->> RC: solve()

  Note over RC: Methods inside RubiksCube class

  RC ->> RC: rotate_face(face, direction)
  RC ->> RC: shuffle(num_moves)
  RC ->> RC: perform_move(move, direction)
  RC ->> RC: solve()
  RC ->> RC: solve_face(color)
  RC ->> RC: align_face(color)
  RC ->> RC: is_face_solved(color)
  RC ->> RC: get_state()

  M ->> RC: get_state()

  Note over M: Example usage:
  M ->> RC: create()
  M ->> RC: shuffle()
  M ->> RC: solve()

```

And this will produce a flow chart:

```mermaid
graph TD

  A[Start] -->|Initialize Cube| B(Initialize RubiksCube)
  B -->|Shuffle Cube| C(Shuffle Cube)
  C -->|Solve Cube| D{Cube Solved?}
  D -- No --> C
  D -- Yes --> E(End)

```

```mermaid
classDiagram
  class RubiksCube {
    -state: Array<Array<String>>
    +RubiksCube()
    +rotate_face(face: String, direction: String)
    +shuffle(num_moves: Integer)
    +perform_move(move: String, direction: String)
    +solve()
    +solve_face(color: String)
    +align_face(color: String)
    +is_face_solved(color: String): Boolean
    +getState(): Array<Array<String>>
  }

  RubiksCube --|> Array

  class Main {
    +main()
  }

  Main --> RubiksCube


  ```

