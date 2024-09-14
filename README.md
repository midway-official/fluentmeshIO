# fluentmeshIO
This Python module provides functionalities to read and visualize Fluent ASCII mesh files. It can parse mesh files, extract node and face data, and create mesh objects for further analysis and visualization.
# Mesh Module / 网格模块

This Python module provides functionalities to read and visualize Fluent ASCII mesh files. It can parse mesh files, extract node and face data, and create mesh objects for further analysis and visualization.

/ 这个 Python 模块提供了读取和可视化 Fluent ASCII 网格文件的功能。它可以解析网格文件，提取节点和面数据，并创建网格对象以便进一步分析和可视化。

## Features / 特性

- Parse Fluent ASCII mesh files to extract node and face data. / 解析 Fluent ASCII 网格文件以提取节点和面数据。
- Create a `Mesh` object to manage and manipulate mesh data. / 创建 `Mesh` 对象以管理和操作网格数据。
- Visualize specified zones of the mesh using 3D plotting. / 使用 3D 绘图可视化网格中的指定区域。

## Requirements / 需求

- Python 3.x
- `matplotlib`
- `numpy`

You can install the required libraries using pip:

/ 你可以使用 pip 安装所需的库：

```bash
pip install matplotlib numpy
Usage / 使用方法
1. Parsing a Mesh File / 解析网格文件
To read and parse a Fluent ASCII mesh file, use the parse_msh_file function. This function will return the node coordinates and face data.

/ 要读取和解析 Fluent ASCII 网格文件，请使用 parse_msh_file 函数。该函数将返回节点坐标和面数据。

from fluentmeshIO import parse_msh_file

# Path to the Fluent ASCII mesh file
# Fluent ASCII 网格文件的路径
file_path = '/path/to/your/msh/file.msh'

# Parse the mesh file
# 解析网格文件
points, faces = parse_msh_file(file_path)
2. Creating and Using the Mesh Object / 创建和使用 Mesh 对象
You can create a Mesh object using the node coordinates and face data. The Mesh class provides methods to manipulate and visualize the mesh.

/ 你可以使用节点坐标和面数据创建 Mesh 对象。Mesh 类提供了操作和可视化网格的方法。


from mesh_module import Mesh

# Create a Mesh object
# 创建 Mesh 对象
mesh = Mesh(points, faces)

# Print Mesh information
# 打印 Mesh 信息
print(mesh)

# Plot faces in specified zones
# 绘制指定区域的面
mesh.plot_face_in_zone([5, 6, 7, 8, 9, 10])
3. Functions / 函数
plot_faces(points, faces, zone_ids): Visualizes the faces in specified zones. / 可视化指定区域的面。
n_head_to_array(input_str): Parses node header information from a string. / 从字符串中解析节点头信息。
f_head_to_array(input_str): Parses face header information from a string. / 从字符串中解析面头信息。
nodes_coordinate_to_array(input_str, dim): Converts node coordinates from a string to a list of coordinates. / 将节点坐标从字符串转换为坐标列表。
face_thread_to_array(input_str, dim): Converts face thread data from a string to a list. / 将面线程数据从字符串转换为列表。
Example / 示例
Here’s an example of how to use the module to read a mesh file and plot specified zones:

/ 下面是一个使用模块读取网格文件并绘制指定区域的示例：

python
复制代码
from mesh_module import Mesh, parse_msh_file

# Path to your Fluent ASCII mesh file
# 你的 Fluent ASCII 网格文件路径
file_path = '/path/to/your/msh/file.msh'

# Parse the mesh file
# 解析网格文件
points, faces = parse_msh_file(file_path)

# Create a Mesh object
# 创建 Mesh 对象
mesh = Mesh(points, faces)

# Print Mesh information
# 打印 Mesh 信息
print(mesh)

# Plot faces in specified zones
# 绘制指定区域的面
mesh.plot_face_in_zone([5, 6, 7, 8, 9, 10])
License / 许可证
This module is licensed under the MIT License. See the LICENSE file for more details.

/ 该模块根据 MIT 许可证授权。有关更多详细信息，请参见 LICENSE 文件。

Contributing / 贡献
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

/ 欢迎贡献！请 fork 仓库并提交包含更改的 pull request。

Contact / 联系方式
For any questions or issues, please open an issue on the GitHub repository or contact [midwayofficial41@gmail.com].

/ 如有任何问题或疑虑，请在 GitHub 仓库中打开 issue 或联系 [midwayofficial41@gmail.com]。
