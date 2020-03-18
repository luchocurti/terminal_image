# Images in the Terminal

## Summary

Insert an image and display it in the Command Prompt (CMD) as a matrix of text characters, at a really low-resolution way.

## Supported files

The images can be BMP, GIF, ICO, JPEG, JPG, PNG, and TIFF.

## Module dependencies

**Pillow** library is used.

If it is not installed, run:

```bash
python -m pip install Pillow
```

## How to download the project

1. Click on the "Clone or download" button and copy the web URL.
2. Create a new folder in Windows, name it "terminal_image" and open it.
3. Right-click => "Git Bash Here"
4. Clone the remote repository to your local directory:

    ```bash
    git clone <https://github.com/luchocurti/terminal_image.git>
    ```

5. Return to the folder and the files will be there.

## How to run it

1. Go to the folder where you have the project files and place there the image you want to use.
2. Open the Command Prompt (cmd.exe) and go to the proyect folder.
3. Run:

    ```bash
    py terminal_image.py image_name.ext [character] [Image_width] [Image_height] [BW]
    ```

Where:

* The `image_name` must contain its extension.
* The desired `character` is optional and, if not defined, a full rectangular will be used. Examples: *, =, &, %, $, #, ...
* The `Image_width` (number of characters) is optional. The default value is 80.
* The `Image_height` (number of characters) is optional. The default value is 25.
* `BW` is an optional value. If it is not used, the image will be printed in colors (defauls case), otherwise, if it is udes, it will be created in Black and White format.

## Some examples

* py terminal_image.py apple.jpg * 38 38

![apple](https://drive.google.com/file/d/1EUZUprgVphWr4nyN6Olt2luPN657VNc7/view?usp=sharing)

* py terminal_image.py coca-cola.jpg C 80 80

![coca-cola](https://drive.google.com/file/d/1jpMlcfwaZatmbDTvPZ0SSn-1yPfG-BL_/view?usp=sharing)

* py terminal_image.py google.jpg █ 84 84

![google](https://drive.google.com/file/d/1e0m1TCO9eBQxSHccs40wUYfJXezzMYJy/view?usp=sharing)

* py terminal_image.py nike.jpg / 83 83

![nike](https://drive.google.com/file/d/1K2moc7x1hRhZLr8PA03KHSBwvvHnK4_w/view?usp=sharing)

* py terminal_image.py real_madrid.png M 38 38

![real_madrid](https://drive.google.com/file/d/1ss3n2poV3wkPc9M3AGhGkRJS0-N6LVjt/view?usp=sharing)

* py terminal_image.py rgb.png # 40 40

![rgb](https://drive.google.com/file/d/1JHg2ycJ5-_VgQwvUfXTp80lP9L_wNZwD/view?usp=sharing)

## Developer contact info

* `luchocurti@gmail.com`

## License

This project is licensed under the open-source license.

## GitHub Guides

[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
