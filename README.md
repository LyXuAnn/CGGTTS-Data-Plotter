
# CGGTTS Data Plotter

# 中文版本readme
## 简介
这个项目包含一个Python脚本，用于处理CGGTTS（Common GNSS Generic Time Transfer Standard）格式的文件。它可以读取指定的CGGTTS文件，计算两个接收器之间的差异，并通过`matplotlib`库生成图表来可视化这些差异。

## 特性
- 支持处理CGGTTS格式文件
- 计算两个接收器之间的差异
- 生成差异散点图
- 统计分析并生成汇总图表

## CGGTTS格式文件的命名规范
CGGTTS格式文件应遵循以下命名规范以确保脚本正确处理：
- `[北斗] `：`[CZI/CZC/CZB][ssss][mjd]`:L3I(B1I&B3I)、L3C(B1C&B2a)、L3B(B1I&B2I)组合频点，站点名为ssss(四位),mjd(五位数)。eg：`CZITF0260.306`
- `[伽利略] `：`[EZ][ssss][mjd]`:L3E(E1 & E5a)
组合频点，站点名为ssss(四位),mjd(五位数)。eg：`EZTF0260.306`
- `[GPS] `：`[GZ][ssss][mjd]`:L3P(C1 or P1 & C2 or P2)组合频点，站点名为ssss(四位),mjd(五位数)。eg：`GZTF0260.306`
- `[格鲁纳斯] `：`[RZ][ssss][mjd]`:L3P(C1 or P1 & C2 or P2)组合频点，站点名为ssss(四位),mjd(五位数)。eg：`RZTF0260.306`

## 输出文件解释
该脚本会生成以下输出文件，以帮助用户理解数据差异和统计分析结果：
- `CZBTF01TF0260.302_diff`: 包含两个接收器差异数据的文本文件。
- `CZBTF01TF0260.302_fig.png`: 散点图，展示两个接收器间的时间差异。
- `CZBTF01TF0260.302_fig_summary.png`: 包含五个子图的汇总图表，展示不同统计指标随时间的变化。
- `CZBTF01TF0260.302_summary`: 总结文件，可能包含所有统计数据的文本摘要。
- `CZBTF01TF0260.302_summary_bymjd`: 按修正儒略日汇总的数据，用于进一步分析和图表生成。
以上解释了CZB频点的输出结果，其余频点同理。

## 安装
确保您的系统已安装Python和必要的依赖项。首先，克隆此仓库到本地：

```
git clone https://github.com/LyXuAnn/CGGTTS-Data-Plotter.git
```

然后，安装所需的Python依赖项：

```
pip install -r requirements.txt
```

## 使用
要使用这个脚本，您需要提供CGGTTS文件的路径以及输出目录。通过命令行参数传递这些信息：

```
python main.py --arg1_flpath1 [第一个接收器对应的CGGTTS文件的绝对路径] --arg2_flpath2 [第二个接收器对应的CGGTTS文件的绝对路径] --arg3_outdir [输出目录]
```

## 贡献
欢迎通过Pull Requests或Issues为这个项目做出贡献。请确保您的代码符合项目的编码标准。


# CGGTTS Data Plotter

# English version
## Introduction
This project includes a Python script for processing files in the CGGTTS (Common GNSS Generic Time Transfer Standard) format. It can read specified CGGTTS files, calculate the differences between two receivers, and generate charts using the `matplotlib` library to visualize these differences.

## Features
- Supports processing CGGTTS format files
- Calculates differences between two receivers
- Generates scatter plots of the differences
- Performs statistical analysis and generates summary charts

## Naming Convention for CGGTTS Format Files
CGGTTS format files should follow the following naming convention to ensure proper handling by the script:
- `[BeiDou] `: `[CZI/CZC/CZB][ssss][mjd]`: L3I (B1I & B3I), L3C (B1C & B2a), L3B (B1I & B2I) combination frequencies, with ssss (four digits) as the station name and mjd (five digits). Example: `CZITF0260.306`
- `[Galileo] `: `[EZ][ssss][mjd]`: L3E (E1 & E5a) combination frequency, with ssss (four digits) as the station name and mjd (five digits). Example: `EZTF0260.306`
- `[GPS] `: `[GZ][ssss][mjd]`: L3P (C1 or P1 & C2 or P2) combination frequency, with ssss (four digits) as the station name and mjd (five digits). Example: `GZTF0260.306`
- `[GLONASS] `: `[RZ][ssss][mjd]`: L3P (C1 or P1 & C2 or P2) combination frequency, with ssss (four digits) as the station name and mjd (five digits). Example: `RZTF0260.306`

## Explanation of Output Files
The script generates the following output files to help users understand data differences and statistical analysis results:
- `CZBTF01TF0260.302_diff`: A text file containing the differences between two receivers' data.
- `CZBTF01TF0260.302_fig.png`: A scatter plot displaying the time differences between two receivers.
- `CZBTF01TF0260.302_fig_summary.png`: A summary chart containing five subplots showing how different statistical metrics change over time.
- `CZBTF01TF0260.302_summary`: A summary file that may contain a textual summary of all statistical data.
- `CZBTF01TF0260.302_summary_bymjd`: Data summarized by Modified Julian Date (MJD) for further analysis and chart generation. The same applies to other frequency points.

## Installation
Ensure that your system has Python and the necessary dependencies installed. First, clone this repository to your local machine:

```
git clone https://github.com/LyXuAnn/CGGTTS-Data-Plotter.git
```

Then, install the required Python dependencies:

```
pip install -r requirements.txt
```


## Usage
To use this script, you need to provide the paths of CGGTTS files for the two receivers and an output directory. Pass this information as command-line arguments:


```
python main.py --arg1_flpath1 [absolute path to the CGGTTS file for the first receiver] --arg2_flpath2 [absolute path to the CGGTTS file for the second receiver] --arg3_outdir [output directory]
```

## Contributions
Contributions to this project are welcome through Pull Requests or Issues. Please ensure that your code adheres to the project's coding standards.
