class Tree_Keyword_Argument(
        TRAIT_Tree_Argument,
):
    __slots__ = ((
        'symbol',                       #   Parser_Symbol
        'value',                        #   Tree_Expression
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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
        'attribute',                    #   Symbol
    ))


class Tree_Delete_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Expression,
):
    __slots__ = (())


class Tree_Store_Attribute(
        Tree_Attribute,
        TRAIT_Tree_Store_Target,
):
    __slots__ = (())


class Tree_Comprehension_Clause_Leaf(
        TRAIT_Tree_Comprehension_Clause,
):
    __slots__ = ((
        'target',                       #   Tree_Expression
        'sequence',                     #   Tree_Expression
        'if_tests',                     #   SomeNativeList of Tree_Expression
    ))


class Tree_Test_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'test',                         #   Tree_Expression
        'body',                         #   Tree_Statement
        'else_clause_0',                #   Tree_Suite_0
    ))


class Tree_For_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'target',                       #   Tree_Target
        'sequence',                     #   Tree_Expression
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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'body',                         #   Tree_Statement
        'except_handlers',              #   FullNativeList of Tree_Except_Handler
        'else_clause_0',                #   Tree_Suite_0
    ))

class Tree_Try_Finally_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
        'target',                       #   None | Tree_Target
        'body',                         #   Tree_Statement
    ))


class Tree_Class_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'name',                         #   Parser_Symbol
        'bases',                        #   SomeNativeList of Tree_Expression
        'body',                         #   Tree_Suite
        'decorator_list',               #   Some_NativeList of Tree_Decorator
    ))


class Tree_Function_Definition(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'name',                         #   Parser_Symbol
        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Suite
        'decorator_list',               #   SomeNativeList of Tree_Decorator
    ))


class Tree_Value_Comprehension(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'element',                      #   Tree_Expression
        'generators',                   #   FullNativeList of Tree_Comprehension
    ))


class Tree_Backquote_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
    ))


class Tree_Binary_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'left',                         #   Tree_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Expression
    ))


class Tree_Call_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'function',                     #   Tree_Expression
        'arguments',                    #   Some_NativeList of Tree_Expression
        'keywords',                     #   Some_NativeList of Tree_Expression
        'star_arguments',               #   None | Tree_Expression
        'keyword_arguments',            #   None | Tree_Expression
    ))


class Tree_Compare_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'left',                         #   Tree_Expression
        'operators',                    #   FullNativeList of Tree_Operator
        'comparators',                  #   FullNativeList of Tree_Expression
    ))


class Tree_Generator_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())

    keyword = 'generator-comprehension'


class Tree_If_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'test',                         #   Tree_Expression
        'body',                         #   Tree_Expression
        'else_expression',              #   Tree_Expression
    ))


class Tree_Logical_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'operator',                     #   Tree_Operator
        'values',                       #   FullNativeList of Tree_Expression
    ))


class Tree_Map_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'keys',                         #   SomeNativeList of Tree_Expression
        'values',                       #   SomeNativeList of Tree_Expression
    ))


class Tree_Lambda_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'parameters',                   #   Tree_Parameter
        'body',                         #   Tree_Expression
    ))


class Tree_List_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())


class Tree_Map_Comprehension(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'key',                          #   Tree_Expression
        'value',                        #   Tree_Expression
        'generators',                   #   FullNativeList of Tree_Comprehension
    ))


class Tree_Number(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'n',                            #   int
    ))


class Tree_Set_Comprehension(Tree_Value_Comprehension):
    __slots__ = (())


class Tree_Set_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'values',                       #   SomeNativeList of Tree_Expression
    ))


class Tree_String(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        's',                            #   Some_Native_String
    ))


class Tree_Unary_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Expression
    ))


class Tree_Yield_Expression(
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   None | Tree_Expression
    ))


class Tree_Except_Handler(
        TRAIT_Tree_Except_Clause,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'type_expression',              #   None | Tree_Expression
        'name_expression',              #   None | Tree_Expression
        'body',                         #   FullNativeList of Tree_Statement
    ))

class Tree_Ellipses_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = (())


class Tree_Extended_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'many',                         #   NativeList of Tree_Index_Clause
    ))


class Tree_Simple_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'value',                        #   Tree_Expression
    ))


class Tree_Slice_Index(
        TRAIT_Tree_Index_Clause,
):
    __slots__ = ((
        'lower',                        #   None | Tree_Expression
        'upper',                        #   None | Tree_Expression
        'step',                         #   None | Tree_Expression
    ))


class Tree_Many_Expression(object):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'elements',                     #   SomeNativeList of Tree_Expression
    ))


class Tree_Evaluate_List(
        Tree_Many_Expression
        TRAIT_Tree_Expression,
):
    __slots__ = (())


class Tree_Evaluate_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Expression,
):
    __slots__ = (())


class Tree_Store_List(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
):
    __slots__ = (())


class Tree_Store_Tuple(
        Tree_Many_Expression,
        TRAIT_Tree_Store_Target,
):
    __slots__ = (())


class Tree_Name(object):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'symbol',                       #   Symbol
    ))


class Tree_Delete_Name(
        Tree_Name,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Name(
        Tree_Name,
        TRAIT_Tree_Expression,
):
    __slots__ = (())


class Tree_Normal_Parameter(
        Tree_Name,
        TRAIT_Tree_Parameter,
):
    __slots__ = (())


class Tree_Store_Name(
        Tree_Name,
        TRAIT_Tree_Store_Target,
):
    __slots__ = (())


@enumeration
class Tree_Operator_Enumeration(
        TRAIT_Tree_Operator,
):
    __slots__ = ((
        'operator_token',               #   String
    ))


class Tree_Parameters_All(
        TRAIT_Tree_Parameter,
):
    __slots__ = ((
        'normal_parameters',            #   SomeNativeList of Tree_NormalParameter
        'tuple_parameter',              #   None | Full_Native_String
        'map_parameter',                #   None | Full_Native_String
        'defaults',                     #   SomeNativeList of Tree_Expression
    ))


class Tree_Subscript_Expression(
        TRAIT_Tree_Delete_Target,
        TRAIT_Tree_Expression,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
        'index',                        #   Tree_Index_Clause
    ))


class Tree_Delete_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Delete_Target,
):
    __slots__ = (())


class Tree_Evaluate_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Expression,
):
    __slots__ = (())


class Tree_Store_Subscript(
        Tree_Subscript_Expression,
        TRAIT_Tree_Store_Target,
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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer
    ))


class Tree_Assert_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'test',                         #   Tree_Expression
        'message',                      #   None | Tree_Expression
    ))


class Tree_Assign_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'targets',                      #   NativeList of Tree_Expression
        'value',                        #   Tree_Expression
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
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'targets',                      #   FullNativeList of Tree_Target
    ))


class Tree_Execute_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'body',                         #   Tree_Expression
        'globals',                      #   None | Tree_Expression
        'locals',                       #   None | Tree_Expression
    ))


class Tree_Expression_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
    ))


class Tree_From_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'module',                       #   Parser_Module_Name
        'names',                        #   FullNativeList of Tree_Symbol_Alias
        'level',                        #   Substantial_Integer
    ))


class Tree_Global_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'names',                        #   FullNativeList of Full_Native_String
    ))


class Tree_Import_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'module_aliases',               #   NativeList of Tree_Module_Alias
    ))


class Tree_Modify_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'left',                         #   Tree_Expression
        'operator',                     #   Tree_Operator
        'right',                        #   Tree_Expression
    ))


class Tree_Pass_Statement(Tree_Keyword_Statement):
    __slots__ = (())


class Tree_Print_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'destination',                  #   None | Tree_Expression
        'values',                       #   SomeNativeList of Tree_Expression
        'newline',                      #   NativeBoolean
    ))


class Tree_Return_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'value',                        #   Tree_Expression
    ))


class Tree_Raise_Statement(
        TRAIT_Tree_Statement,
        TRAIT_Tree_Suite,
        TRAIT_Tree_Suite_0,
):
    __slots__ = ((
        'line_number',                  #   Positive_Integer
        'column',                       #   Substantial_Integer

        'type',                         #   None | Tree_Expression
        'instance',                     #   None | Tree_Expression
        'traceback',                    #   None | Tree_Expression
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
        'name',                         #   Full_Native_String

        #
        #   Interface Tree_Context
        #
       #@replace
        'is_tree_delete_context',       #   NativeBoolean
       #@replace
        'is_tree_load_context',         #   NativeBoolean
       #@replace
        'is_tree_parameter_context',    #   NativeBoolean
       #@replace
        'is_tree_store_context',        #   NativeBoolean
    ))
