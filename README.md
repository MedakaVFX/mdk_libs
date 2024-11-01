# mdklibs
---
VFX用Pythonライブラリ

## v0.0.1
- Added : 基本構造作成
- Added : mdklibs.path モジュール


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


## Examples
``` python
import mdklibs as mdk

mdk.version()
# v0.0.1

mdk.name()
# mdklibs

mdk.path.get_versions('c:/t-yamagishi/v01/asset_v0002.mb')
# ['v01', 'v0002']

mdk.path.version_up('c:/t-yamagishi/v01/asset_v0002.mb')
# 'c:/t-yamagishi/v02/asset_v0003.mb'
```

