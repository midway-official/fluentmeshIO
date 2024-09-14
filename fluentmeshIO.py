import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import re

def plot_faces(points, faces, zone_ids):
    """
    绘制指定 zone_id 的面。
    
    :param points: 点的坐标列表，每个点是一个三元组 (x, y, z)。
    :param faces: 面的列表，每个面是一个包含点索引和其他数据的列表。
    :param zone_ids: 要绘制的 zone_id 列表。
    """
    if isinstance(zone_ids, int):
        zone_ids = [zone_ids]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    faces_to_plot = []

    for face in faces:
        if face[6] in zone_ids:
            n0, n1, n2, n3 = face[:4]
            p0 = points[n0-1]
            p1 = points[n1-1]
            p2 = points[n2-1]
            p3 = points[n3-1]
            face_vertices = np.array([p0, p1, p2, p3, p0])
            faces_to_plot.append(face_vertices)

    poly3d = Poly3DCollection(faces_to_plot, edgecolor='k', linewidths=0.5, alpha=0.5)
    ax.add_collection3d(poly3d)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x, y, z = zip(*[point for point in points])
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))

    plt.show()

def n_head_to_array(input_str):
    elements = input_str.split()
    if len(elements) < 5:
        raise ValueError("输入cells/nodes总述必须包含至少6个要点")
    return [int(elements[0]), int(elements[1]), int(elements[2], 16), int(elements[3]), int(elements[4])]

def f_head_to_array(input_str):
    elements = input_str.split()
    if len(elements) < 5:
        raise ValueError("输入cells/nodes总述必须包含至少6个要点")
    return [int(elements[0], 16), int(elements[1], 16), int(elements[2], 16), int(elements[3], 16), int(elements[4])]

def nodes_coordinate_to_array(input_str, dim):
    elements = input_str.split()
    if dim not in [2, 3]:
        raise ValueError("mesh维度必须是2或3")
    if len(elements) % dim != 0:
        raise ValueError("元素数量必须是维度的倍数")
    return [[float(num) for num in elements[i:i + dim]] for i in range(0, len(elements), dim)]

def face_thread_to_array(input_str, dim):
    elements = input_str.split()
    return [[int(num, 16) for num in elements[i:i + dim]] for i in range(0, len(elements), dim)]

class Mesh:
    def __init__(self, points, faces):
        self.points = points
        self.faces = faces

    def get_point(self, index):
        return self.points[index - 1]

    def get_face(self, index):
        return self.faces[index - 1]

    def add_point(self, coordinates):
        self.points.append(coordinates)

    def add_face(self, face_data):
        self.faces.append(face_data)

    def find_faces_by_point_id(self, point_id):
        point_id = int(point_id)
        faces_with_point = []
        for face in self.faces:
            n0, n1, n2, n3, c0, c1, zone_id, first_index, last_index, bc_type, face_type = face
            if point_id in [n0, n1, n2, n3]:
                faces_with_point.append(face)
        return faces_with_point

    def plot_face_in_zone(self, zones):
        plot_faces(self.points, self.faces, zones)

    def __str__(self):
        return f'Points: {self.points}\nFaces: {self.faces}'

def parse_msh_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # nodes总述字段
    pattern1 = r'\(10\s*\(([^)]+)\)\)'
    nodes_heads = re.findall(pattern1, content)
    node_overview = [n_head_to_array(head) for head in nodes_heads]

    # nodes坐标字段
    pattern2 = r'\(10\s*\(([^)]+)\)\s*\(([\s\S]*?)\)\)'
    nodes_datas_list = re.findall(pattern2, content)
    node_data = []
    for part_info, coordinates in nodes_datas_list:
        node_data.extend(nodes_coordinate_to_array(coordinates, 3))

    # face总述字段
    pattern3 = r'\(13\s*\(([^)]+)\)\)'
    face_heads = re.findall(pattern3, content)
    face_overview = [f_head_to_array(head) for head in face_heads]

    # face线程字段
    pattern4 = r'\(13\s*\(([^)]+)\)\s*\(([\s\S]*?)\)\)'
    faces_datas0 = re.findall(pattern4, content)

    faces_heads = [f_head_to_array(t[0]) for t in faces_datas0]
    faces_thread = [face_thread_to_array(t[1], 6) for t in faces_datas0]

    face_head_list = []
    for face in faces_heads:
        zone_id, first_index, last_index, bc_type, face_type = face
        for index in range(first_index, last_index + 1):
            face_head_list.append([zone_id, index, bc_type, face_type])

    face_thread_list = [item for sublist in faces_thread for item in sublist]
    face_data = [face_thread_list[i] + face_head_list[i] for i in range(len(face_head_list))]

    return node_data, face_data
