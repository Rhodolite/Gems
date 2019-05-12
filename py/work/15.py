class Tree_Keyword_Argument(
        TRAIT_Tree_Argument,
):
    __slots__ = ((
        'symbol',                       #   Parser_Symbol
        'value',                        #   Tree_Value_Expression
    ))


class Tree_Module_Alias_Leaf(
        TRAIT_Tree_Module_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Module_Name
        'as_name',                      #   Parser_Symbol
    ))


class Tree_Symbol_Alias_Leaf(
        TRAIT_Tree_Symbol_Alias,
):
    __slots__ = ((
        'name',                         #   Parser_Symbol
        'as_name',                      #   Parser_Symbol
    ))


class Tree_Attribute(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
        'attribute',                    #   Parser_Symbol
    ))


class Tree_Delete_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = (())


class Tree_Store_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = (())


class Tree_Comprehension_Clause_Leaf(
        TRAIT_Tree_Comprehension_Clause,
):
    __slots__ = ((
        'target',                       #   Tree_Value_Expression
        'sequence',                     #   Tree_Value_Expression
        'if_tests',                     #   Native_List of Tree_Value_Expression
    ))


class Tree_Test_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'test',                         #   Tree_Value_Expression
        'body',                         #   Tree_Statement
        'else_clause_0',                #   Tree_Suite_0
    ))


class Tree_For_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'target',                       #   Tree_Target
        'sequence',                     #   Tree_Value_Expression
        'body',                         #   Tree_Statement
        'else_clause_0',                #   Tree_Suite_0
    ))


class Tree_If_Statement(Tree_Test_Statement):
    __slots__ = (())

    keyword = 'if'


class Tree_Try_Except_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'body',                         #   Tree_Statement
        'except_handlers',              #   Full_Native_List of Tree_Except_Handler
        'else_clause_0',                #   Tree_Suite_0
    ))

class Tree_Try_Finally_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'body',                         #   Tree_Statement
        'finally_body',                 #   Tree_Statement
    ))


class Tree_While_Statement(Tree_Test_Statement):
    __slots__ = (())

    keyword = 'while'


class Tree_With_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
        'target',                       #   Tree_Store_Target_0
        'body',                         #   Tree_Statement
    ))


class Tree_Class_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'name',                         #   Parser_Symbol
        'bases',                        #   Native_List of Tree_Value_Expression
        'body',                         #   Tree_Suite
        'decorator_list',               #   Native_List of Tree_Decorator
    ))


class Tree_Function_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'name',                         #   Parser_Symbol
        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Suite
        'decorator_list',               #   Native_List of Tree_Decorator
    ))


class Tree_Value_Comprehension(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'element',                      #   Tree_Value_Expression
        'generators',                   #   Full_Native_List of Tree_Comprehension
    ))


class Tree_Backquote_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
    ))


class Tree_Binary_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'left',                         #   Tree_Value_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Value_Expression
    ))


class Tree_Call_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'function',                     #   Tree_Value_Expression
        'arguments',                    #   Native_List of Tree_Value_Expression
        'keywords',                     #   Native_List of Tree_Value_Expression
        'star_arguments',               #   Tree_Value_Expression_0
        'keyword_arguments',            #   Tree_Value_Expression_0
    ))


class Tree_Compare_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'left',                         #   Tree_Value_Expression
        'operators',                    #   Full_Native_List of Tree_Operator
        'comparators',                  #   Full_Native_List of Tree_Value_Expression
    ))


class Tree_Generator_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())

    keyword = 'generator-comprehension'


class Tree_If_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'test',                         #   Tree_Value_Expression
        'body',                         #   Tree_Value_Expression
        'else_expression',              #   Tree_Value_Expression
    ))


class Tree_Logical_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'operator',                     #   Tree_Operator
        'values',                       #   Full_Native_List of Tree_Value_Expression
    ))


class Tree_Map_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'keys',                         #   Native_List of Tree_Value_Expression
        'values',                       #   Native_List of Tree_Value_Expression
    ))


class Tree_Lambda_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Value_Expression
    ))


class Tree_List_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())


class Tree_Map_Comprehension(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'key',                          #   Tree_Value_Expression
        'value',                        #   Tree_Value_Expression
        'generators',                   #   Full_Native_List of Tree_Comprehension
    ))


class Tree_Set_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())


class Tree_Set_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'values',                       #   Native_List of Tree_Value_Expression
    ))


class Tree_Number_Literal(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'n',                            #   Number
    ))


class Tree_String_Literal(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        's',                            #   String
    ))


class Tree_Unary_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Value_Expression
    ))


class Tree_Yield_Expression(
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression_0
    ))


class Tree_Except_Handler(
        TRAIT_Tree_Except_Clause,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'type_expression',              #   Tree_Value_Expression_0
        'target_expression',            #   Tree_Store_Target_0
        'body',                         #   Tree_Suite
    ))


class Tree_Ellipses_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = (())


class Tree_Extended_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'many',                         #   Full_Native_List of Tree_Index_Clause
    ))


class Tree_Simple_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'value',                        #   Tree_Value_Expression
    ))


class Tree_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'lower',                        #   Tree_Value_Expression_0
        'upper',                        #   Tree_Value_Expression_0
        'step',                         #   Tree_Value_Expression_0
    ))


class Tree_Many_Expression(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'elements',                     #   Native_List of (Tree_Store_Target | Tree_Value_Expression)
    ))


class Tree_Evaluate_List(
        Tree_Many_Expression
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Native_List of Tree_Value_Expression
    ))


class Tree_Evaluate_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Native_List of Tree_Value_Expression
    ))


class Tree_Store_List(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Native_List of Tree_Store_Target
    ))



class Tree_Store_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = ((
    #   'elements',                     #   Inherited from `Tree_Many_Expression`; but type changes to:
    #                                   #       Native_List of Tree_Store_Target
    ))




class Tree_Name_Branch(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbol',                       #   Parser_Symbol
    ))


class Tree_Delete_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = (())


class Tree_Store_Name(
        Tree_Name_Branch,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = (())


@enumeration
class Tree_Operator_Enumeration(
        TRAIT_Tree_Operator,
):
    __slots__ = ((
        'operator_token',               #   String
    ))

class Tree_Special_Parameter(object):
    __slots__ = ((
        'symbol',                       #   Parser_Symbol
    ))

class Tree_Map_Parameter(
        Tree_Special_Parameter,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = (())

class Tree_Keyword_Parameter(
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbol',                       #   Parser_Symbol
        'value',                        #   Tree_Value_Expression
    ))

class Tree_Normal_Parameter(
        Tree_Name_Branch,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = (())

class Tree_Star_Parameter(
        Tree_Special_Parameter,
        TRAIT_Tree_Parameter,
        TRAIT_Tree_Parameter_0,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0,
):
    __slots__ = (())


class Tree_Parameter_Tuple_Leaf(
        tuple,
        TRAIT_Tree_Parameter_Tuple,
        TRAIT_Tree_Parameter_Tuple_0
):
    __slots__ = (())


class Tree_Subscript_Expression(object):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
        'index',                        #   Tree_Index_Clause
    ))


class Tree_Delete_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Value_Expression,
        TRAIT_Tree_Value_Expression_0,
):
    __slots__ = (())


class Tree_Store_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Store_Target,
        TRAIT_Tree_Store_Target_0,
):
    __slots__ = (())


#
#   Tree: Keyword Statement - Base class of `break` and `pass` statement.
#
class Tree_Keyword_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer
    ))


class Tree_Assert_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'test',                         #   Tree_Value_Expression
        'message',                      #   Tree_Value_Expression_0
    ))


class Tree_Assign_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'targets',                      #   Full_Native_List of Tree_Store_Target
        'value',                        #   Tree_Value_Expression
    ))


class Tree_Break_Statement(Tree_Keyword_Statement):
    __slots__ = (())


class Tree_Continue_Statement(Tree_Keyword_Statement):
    __slots__ = (())


class Tree_Delete_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'targets',                      #   Full_Native_List of Tree_Target
    ))


class Tree_Execute_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'body',                         #   Tree_Value_Expression
        'globals',                      #   Tree_Value_Expression_0
        'locals',                       #   Tree_Value_Expression_0
    ))


class Tree_Expression_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression
    ))


class Tree_From_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'module',                       #   Parser_Module_Name
        'names',                        #   Full_Native_List of Tree_Symbol_Alias
        'level',                        #   Avid_Native_Integer
    ))


class Tree_Global_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'symbols',                      #   Parser_Symbol_Tuple
    ))


class Tree_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'module_aliases',               #   Full_Native_List of Tree_Module_Alias
    ))


class Tree_Modify_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'left',                         #   Tree_Value_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Value_Expression
    ))


class Tree_Pass_Statement(Tree_Keyword_Statement):
    __slots__ = (())


class Tree_Print_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'destination',                  #   Tree_Value_Expression_0
        'values',                       #   Native_List of Tree_Value_Expression
        'newline',                      #   Native_Boolean
    ))


class Tree_Return_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Native_Integer
        'column',                       #   Avid_Native_Integer

        'value',                        #   Tree_Value_Expression_0
    ))


class Tree_Raise_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Native_Positive_Integer
        'column',                       #   Avid_Native_Integer

        'type',                         #   Tree_Value_Expression_0
        'instance',                     #   Tree_Value_Expression_0
        'traceback',                    #   Tree_Value_Expression_0
    ))


class Tree_Suite_Leaf(
        tuple,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = (())


@enumeration
class Tree_Context_Enumeration(
        TRAIT_Tree_Context,
):
    __slots__ = ((
        'name',                         #   String

        #
        #   Interface Tree_Context
        #
       #@replace
        'is_tree_delete_context',       #   Native_Boolean
       #@replace
        'is_tree_load_context',         #   Native_Boolean
       #@replace
        'is_tree_parameter_context',    #   Native_Boolean
       #@replace
        'is_tree_store_context',        #   Native_Boolean
    ))
