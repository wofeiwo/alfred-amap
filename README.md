高德地图搜索插件
==============

[![License](https://img.shields.io/github/license/wofeiwo/alfred-amap.svg?label=License)](https://github.com/wofeiwo/alfred-amap/blob/master/LICENSE) [![Release](https://img.shields.io/github/release/wofeiwo/alfred-amap.svg?label=Release)](https://github.com/wofeiwo/alfred-amap/releases)

通过Alfred搜索高德地图的Workflow。功能和之前的[`alfred-baidu-map`](https://github.com/wofeiwo/alfred-baidu-map)一模一样。（换了一个东家，所以也做个高德的版本吧）

使用方法：
- 首先输入"amapsetl"+空格+城市名，设置默认搜索城市地点;
- （可选）输入"amapak"+空格+你自己的高德地图开放平台WebAPI AK值，避免公用key超过限制。默认使用自带的API ak;
- 输入"amap"+空格+搜索关键字即可。然后就等他出结果，回车或者cmd+数字就能打开默认浏览器进入地图页面进入地图页面查看搜索结果。
- Tips: 可以直接输入"amap"+空格+"A到B"或"A去B"，回车后可以直接显示路线图

安装：请安装alfred之后，买了alfred的powerpack并激活，[下载workflow文件](https://github.com/wofeiwo/alfred-amap/releases)，双击安装即可。 

ChangeLog
==============

- 1.0.1 (2018-10-08): 修复了设置AK时错误写入{query}的bug #2。现在应该会真正写入您所输入的正确AKey。
- 1.0.0 (2018-02-12): 从[`alfred-baidu-map`](https://github.com/wofeiwo/alfred-baidu-map)的功能完全copy而来，换了一个数据源为高德。