# Start Menu / Tiles Editor

Windows 10 Start Menu / Tiles customizer

![SC1](https://github.com/Gwynevere/TilesEditor/blob/main/blob/assets/yellow-black.PNG)
![SC2](https://github.com/Gwynevere/TilesEditor/blob/main/blob/assets/yellow-black-fs.PNG)
![SC3](https://github.com/Gwynevere/TilesEditor/blob/main/blob/assets/red-black-fs.PNG)
![SC4](https://github.com/Gwynevere/TilesEditor/blob/main/blob/assets/red-grey-fs.PNG)


# Installation

Download the [latest release](https://github.com/Gwynevere/TilesEditor/releases) then extract content to a folder

# Config

The script will edit any tile that validate the following constraints :
- tile shortcut file is in search folder `tiles_locations`
- tile image is in search folder `path_images`
- tile shortcut file name matches image file name

If any image is in `path_background_images` it will be applied as a background for the tile

#### `config.json` file

- `tiles_locations` list of folders containing windows shortcuts `.lnk` pinned in start menu
- `path_images` images folder path to use for tiles
- `path_background_images` background image folder path to use for tiles (random image per tile is chosen if more than one is available)
- `text_color` text color (`light` | `dark`)
- `text_color_fill` text color in fill mode (`light` | `dark`)

#### Images names properties
- Tile image can be set to fill mode, image will fill all the tile square by adding `.fill` to file name. eg: to set vortex tile image into fill mode I will set `Vortex.fill.png` as the image file name 

>To change a tile background color and image, the `.lnk` file name (found in `tiles_locations`) must be
the same as the corresponding `image` name (found in `path_images`)

>Disable Windows transparency for better results

# Resources
Icons link [icons8](https://icons8.com/icons)

# License

Copyright [2021] [Gwynevere]

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "
AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
