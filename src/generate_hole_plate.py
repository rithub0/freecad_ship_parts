import FreeCAD as App
import Part

# モデル寸法設定（mm）
WIDTH = 1000
HEIGHT = 500
THICKNESS = 12
HOLE_DIAMETER = 200

# ドキュメント新規作成
doc = App.newDocument("SteelPlate")

# ベース平板
plate = Part.makeBox(WIDTH, HEIGHT, THICKNESS)

# 中央の円穴
hole_pos = App.Vector(WIDTH/2, HEIGHT/2, 0)
hole = Part.makeCylinder(HOLE_DIAMETER / 2, THICKNESS, hole_pos)

# 穴を開けた結果
result = plate.cut(hole)
Part.show(result)
doc.recompute()

# 任意の保存（ローカル実行時に必要に応じて設定）
# Part.export([result], "hole_plate.stl")
