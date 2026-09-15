# some-icons

搜集一些有趣的图标

## 来源

### 编程语言图标（方）

- F#: https://fsharp.org/img/logo/fsharp.svg
- Rhombus: https://rhombus-lang.org/rhombus-logo.svg
- Haskell: https://www.haskell.org/img/haskell-logo.svg

### 编程语言图标（圆）

- C++: https://github.com/isocpp/logos/blob/master/cpp_logo.svg
- Racket: https://racket-lang.org/img/racket-logo.svg
- Common Lisp: https://commons.wikimedia.org/wiki/File:Lisp_logo.svg
- Fortran: https://github.com/fortran-lang/fortran-lang.org/blob/master/assets/img/fortran-logo.svg

### 编程语言（其他）

- C++ 核心指南: https://github.com/isocpp/logos/blob/master/cpp_core_guidelines/cpp_core_guidelines_logo.svg
- Ferris (Rust): https://rustacean.net/assets/cuddlyferris.svg

### 其他

- 哔哩哔哩网页端 favicon: https://www.svgrepo.com/svg/345504/bilibili
- RSS Feed: http://www.feedicons.com/download/feedicons-devkit.zip 中的 default/feed-icon.svg

### 补充说明

- 关于 Haskell 官方图标:
    - 做了修改。去除了文字部分，留下了图形部分。
- 关于 Common Lisp 图标:
    - 原型: https://common-lisp.net/static/imgs/lisplogo.png
    - SVG 格式由用户 [Jooja](https://commons.wikimedia.org/wiki/User:Jooja) 模仿绘制。
- 关于哔哩哔哩网页端 favicon:
    - 做了修改。参照目前的官方 favicon 修改了颜色。
    - 备选 1: https://lobehub.com/zh/icons/bilibili
    - 备选 2: https://fontawesome.com/icons/brands/solid/bilibili
    - 原型: https://www.bilibili.com/favicon.ico
- 放弃了 Gopher 图标。
    - 出处: https://go.dev/blog/gopher
- 放弃了埃舍尔的蜥蜴。
    - 和它有关的一篇文章: https://www.seanmichaelragan.com/html/%5B2008-04-18%5D_MC_Escher_lizard_vector_art.shtml

## 用途

可用于软件内部装饰，还可以用于定制贴纸、立牌、钥匙串挂件等。

## 注意

部分从网上下载的文件和本项目中的文件因换行符不同而不同。本项目 `.gitattributes` 中的设置使得文本文件都以 LF 换行，没有 CRLF。

## 构建

环境要求：

- [Python 3](https://www.python.org/)
- [Inkscape](https://inkscape.org/) 1.0 及以上版本

在根目录运行 `batch_convert.py` 即可。

我在编写本项目时使用的 Inkscape 版本： `Inkscape 1.4.2 (f4327f4, 2025-05-13)`
