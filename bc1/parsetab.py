
# /Users/jpercent/github/bc/bc1/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '502ED33F2920A37E1E2369F65B41BD51'
    
_lr_action_items = {'LPAREN':([0,4,6,7,8,9,10,],[4,4,4,4,4,4,4,]),'DIVIDE':([1,2,5,11,12,13,14,15,16,17,],[-8,8,-9,8,-6,-4,-5,8,8,-7,]),'PLUS':([1,2,5,11,12,13,14,15,16,17,],[-8,9,-9,9,-6,-4,-5,-2,-3,-7,]),'NUMBER':([0,4,6,7,8,9,10,],[1,1,1,1,1,1,1,]),'TIMES':([1,2,5,11,12,13,14,15,16,17,],[-8,7,-9,7,-6,-4,-5,7,7,-7,]),'$end':([1,2,3,5,12,13,14,15,16,17,],[-8,-1,0,-9,-6,-4,-5,-2,-3,-7,]),'RPAREN':([1,5,11,12,13,14,15,16,17,],[-8,-9,17,-6,-4,-5,-2,-3,-7,]),'NAME':([0,4,6,7,8,9,10,],[5,5,5,5,5,5,5,]),'MINUS':([0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[6,-8,10,6,-9,6,6,6,6,6,10,-6,-4,-5,-2,-3,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,6,7,8,9,10,],[2,11,12,13,14,15,16,]),'statement':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','bc.py',66),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','bc.py',70),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','bc.py',71),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','bc.py',72),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','bc.py',73),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','bc.py',80),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','bc.py',84),
  ('expression -> NUMBER','expression',1,'p_expression_number','bc.py',88),
  ('expression -> NAME','expression',1,'p_expression_name','bc.py',92),
]
