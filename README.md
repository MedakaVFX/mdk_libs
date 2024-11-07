# mdklibs
---
VFX用Pythonライブラリ
- Linux、Mac、Windowsクロスプラットフォーム

## v0.0.1
- added : 基本構造作成
- added : mdklibs.file モジュール
- added : mdklibs.path モジュール


## Recommended 
| Name | Version | Description |
| ---- | ---- | ---- |
| Python | 3.12.x |
| PySide | 6 (Qt 6.8.0.1) |


## Environment Variables
- 環境変数は`大文字` (UNIX系は大文字、小文字が指定出来るが、Windowsが大文字、小文字の概念が無い場合があるため)

| Vars | Description |
| ---- | ---- |
| MDK_DEBUG | デバッグモード 0 or 1 |

## Comment
- added : test module #1
- changed : test #1
- updated : test #1
- fixed : test #1

## Examples
``` python
import mdklibs as mdk

mdk.version()
# v0.0.1

mdk.name()
# mdklibs


# ---------------------
# mdk.libs
mdk.path.get_versions('c:/t-yamagishi/v01/asset_v0002.mb')
# ['v01', 'v0002']

mdk.path.version_up('c:/t-yamagishi/v01/asset_v0002.mb')
# 'c:/t-yamagishi/v02/asset_v0003.mb'

mdk.path.open_in_explorer('c:/t-yamagishi/v01/asset_v0002.mb')

# ---------------------
# mdk.file
mdk.file.open_file('C:\Users\ta_yamagishi\temp\pic001.png')
mdk.file.save_text(<filepath>, 'test')
mdk.file.save_json(<filepath>, <dict>)
mdk.file.save_csv(<filepath>, <list[list[str]]>)
```

