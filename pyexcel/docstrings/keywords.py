"""
    pyexcel.docstrings.keywords
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Reusible docstrings for keywords in signature functions

    :copyright: (c) 2015-2017 by Onni Software Ltd.
    :license: New BSD License
"""
CSV_PARAMS = """
**Parameters related to csv file format**

for csv, `fmtparams <https://docs.python.org/release/3.1.5/
library/csv.html#dialects-and-formatting-parameters>`_ are accepted

delimiter :
    field separator

lineterminator :
    line terminator

encoding:
    csv specific. Specify the file encoding the csv file. For example:
    encoding='latin1'. Especially, encoding='utf-8-sig' would add utf 8
    bom header if used in renderer, or would parse a csv with utf brom header
    used in parser.

escapechar :
    A one-character string used by the writer to escape the
    delimiter if quoting is set to QUOTE_NONE and the quotechar if
    doublequote is False.

quotechar :
    A one-character string used to quote fields containing special
    characters, such as the delimiter or quotechar, or which
    contain new-line characters. It defaults to '"'

quoting :
    Controls when quotes should be generated by the writer and
    recognised by the reader. It can take on any of the QUOTE_*
    constants (see section Module Contents) and defaults to QUOTE_MINIMAL.

skipinitialspace :
    When True, whitespace immediately following the delimiter is ignored.
    The default is False.

pep_0515_off :
    When True in python version 3.6, PEP-0515 is turned on.
    The default is False

"""

XLRD_PARAMS = """
**Parameters related to xls file format:**
    Please note the following parameters apply to pyexcel-xls.
    more details can be found in :func:`xlrd.open_workbook`

logfile:
    An open file to which messages and diagnostics are written.

verbosity:
    Increases the volume of trace material written to the logfile.

use_mmap:
    Whether to use the mmap module is determined heuristically.
    Use this arg to override the result.

    Current heuristic: mmap is used if it exists.

encoding_override:
     Used to overcome missing or bad codepage information
     in older-version files.

formatting_info:
     The default is False, which saves memory.

     When True, formatting information will be read from the spreadsheet
     file. This provides all cells, including empty and blank cells.
     Formatting information is available for each cell.

ragged_rows:
     The default of False means all rows are padded out with empty
     cells so that all rows have the same size as found in ncols.

     True means that there are no empty cells at the ends of rows. This
     can result in substantial memory savings if rows are of widely
     varying sizes. See also the row_len() method.
"""

OPTIONAL_BOOK_PARAMS = """
sheets:
    a list of mixed sheet names and sheet indices to be read. This is
    done to keep Pandas compactibility. With this parameter, more than
    one sheet can be read and you have the control to read the sheets
    of your interest instead of all available sheets.

"""

OPTIONAL_PARAMS = """
auto_detect_float :
    defaults to True

auto_detect_int :
    defaults to True

auto_detect_datetime :
    defaults to True

ignore_infinity :
    defaults to True

library :
    choose a specific pyexcel-io plugin for reading

source_library :
    choose a specific data source plugin for reading

parser_library :
    choose a pyexcel parser plugin for reading

skip_hidden_sheets:
     default is True. Please toggle it to read hidden sheets

"""

FILE_PARAMS = """
file_name :
    a file with supported file extension

file_content :
    the file content

file_stream :
    the file stream

file_type :
     the file type in *file_content* or *file_stream*
"""

SKIPPING_FUNC_PROTOCOL = """
    The protocol is
    to return pyexcel_io.constants.SKIP_DATA if skipping data,
    pyexcel_io.constants.TAKE_DATA to read data,
    pyexcel_io.constants.STOP_ITERATION to exit the reading procedure
"""

PAGINATION_PARAMS = (
    """
start_row : int
    defaults to 0. It allows you to skip rows at the begginning

row_limit: int
    defaults to -1, meaning till the end of the whole sheet. It allows
    you to skip the tailing rows.

start_column : int
    defaults to 0. It allows you to skip columns on your left hand side

column_limit: int
    defaults to -1, meaning till the end of the columns. It allows
    you to skip the tailing columns.

skip_row_func:
    It allows you to write your own row skipping functions.
"""
    + SKIPPING_FUNC_PROTOCOL
    + """
skip_column_func:
    It allows you to write your own column skipping functions.
"""
    + SKIPPING_FUNC_PROTOCOL
    + """
skip_empty_rows: bool
    Defaults to False. Toggle it to True if the rest of empty rows are
    useless, but it does affect the number of rows.

row_renderer:
    You could choose to write a custom row renderer when the data is being
    read.
"""
)

SOURCE_PARAMS = (
    FILE_PARAMS
    + """
session :
    database session

table :
    database table

model:
    a django model

adict:
    a dictionary of one dimensional arrays

url :
    a download http url for your excel file

with_keys :
    load with previous dictionary's keys, default is True

records :
    a list of dictionaries that have the same keys

array :
    a two dimensional array, a list of lists

sheet_name :
    sheet name. if sheet_name is not given, the default
    sheet at index 0 is loaded

"""
    + PAGINATION_PARAMS
    + OPTIONAL_PARAMS
    + CSV_PARAMS
    + XLRD_PARAMS
)

SOURCE_PARAMS_TABLE = """
Not all parameters are needed. Here is a table

========================== =========================================
source                     parameters
========================== =========================================
loading from file          file_name, sheet_name, keywords
loading from string        file_content, file_type, sheet_name, keywords
loading from stream        file_stream, file_type, sheet_name, keywords
loading from sql           session, table
loading from sql in django model
loading from query sets    any query sets(sqlalchemy or django)
loading from dictionary    adict, with_keys
loading from records       records
loading from array         array
loading from an url        url
========================== =========================================
"""

DEST_FILE_PARAMS = """
dest_file_name:
    another file name.

dest_file_type:
    this is needed if you want to save to memory
"""

DEST_PARAMS = (
    DEST_FILE_PARAMS
    + """
dest_session:
    the target database session

dest_table:
    the target destination table

dest_model:
    the target django model

dest_mapdict:
    a mapping dictionary
    see :meth:`pyexcel.Sheet.save_to_memory`

dest_initializer:
    a custom initializer function for table or model

dest_mapdict:
    nominate headers

dest_batch_size:
    object creation batch size.
    it is Django specific

dest_library:
    choose a specific pyexcel-io plugin for writing

dest_source_library:
    choose a specific data source plugin for writing

dest_renderer_library:
    choose a pyexcel parser plugin for writing

"""
)

DEST_PARAMS_TABLE = """
================= =============================================
Saving to source  parameters
================= =============================================
file              dest_file_name, dest_sheet_name,
                  keywords with prefix 'dest'
memory            dest_file_type, dest_content,
                  dest_sheet_name, keywords with prefix 'dest'
sql               dest_session, dest_table,
                  dest_initializer, dest_mapdict
django model      dest_model, dest_initializer,
                  dest_mapdict, dest_batch_size
================= =============================================
"""

DEST_BOOK_PARAMS = (
    DEST_FILE_PARAMS
    + """
dest_session :
    the target database session

dest_tables :
    the list of target destination tables

dest_models :
    the list of target destination django models

dest_mapdicts :
    a list of mapping dictionaries

dest_initializers :
    table initialization functions

dest_mapdicts :
    to nominate a model or table fields. Optional

dest_batch_size :
    batch creation size. Optional
"""
)

SOURCE_BOOK_PARAMS = (
    FILE_PARAMS
    + """
session :
    database session

tables :
    a list of database table

models :
    a list of django models

bookdict :
    a dictionary of two dimensional arrays

url :
    a download http url for your excel file
"""
    + OPTIONAL_BOOK_PARAMS
    + OPTIONAL_PARAMS
    + CSV_PARAMS
)

SOURCE_BOOK_PARAMS_TABLE = """
Here is a table of parameters:

========================== ===============================
source                     parameters
========================== ===============================
loading from file          file_name, keywords
loading from string        file_content, file_type, keywords
loading from stream        file_stream, file_type, keywords
loading from sql           session, tables
loading from django models models
loading from dictionary    bookdict
loading from an url        url
========================== ===============================

Where the dictionary should have text as keys and two dimensional
array as values.
"""


I_NOTE = """
for csv, csvz file formats, file handles will be left open.
for xls, ods file formats, the file is read all into memory and
is close afterwards.
for xlsx, file handles will be left open in python 2.7 - 3.5 by
pyexcel-xlsx(openpyxl).
In other words, pyexcel-xls, pyexcel-ods, pyexcel-ods3 won't leak
file handles.
"""


EXAMPLE_NOTE_PAGINATION = """
**Examples on start_row, start_column**

.. testcode::
   :hide:

    >>> import sys
    >>> if sys.version_info[0] < 3:
    ...     from StringIO import StringIO
    ... else:
    ...     from io import StringIO
    >>> from pyexcel_io._compact import OrderedDict

Let's assume the following file is a huge csv file:

.. code-block:: python

   >>> import datetime
   >>> import pyexcel as pe
   >>> data = [
   ...     [1, 21, 31],
   ...     [2, 22, 32],
   ...     [3, 23, 33],
   ...     [4, 24, 34],
   ...     [5, 25, 35],
   ...     [6, 26, 36]
   ... ]
   >>> pe.save_as(array=data, dest_file_name="your_file.csv")

And let's pretend to read partial data:

.. code-block:: python

   >>> pe.get_sheet(file_name="your_file.csv", start_row=2, row_limit=3)
   your_file.csv:
   +---+----+----+
   | 3 | 23 | 33 |
   +---+----+----+
   | 4 | 24 | 34 |
   +---+----+----+
   | 5 | 25 | 35 |
   +---+----+----+

And you could as well do the same for columns:

.. code-block:: python

   >>> pe.get_sheet(file_name="your_file.csv", start_column=1, column_limit=2)
   your_file.csv:
   +----+----+
   | 21 | 31 |
   +----+----+
   | 22 | 32 |
   +----+----+
   | 23 | 33 |
   +----+----+
   | 24 | 34 |
   +----+----+
   | 25 | 35 |
   +----+----+
   | 26 | 36 |
   +----+----+

Obvious, you could do both at the same time:

.. code-block:: python

   >>> pe.get_sheet(file_name="your_file.csv",
   ...     start_row=2, row_limit=3,
   ...     start_column=1, column_limit=2)
   your_file.csv:
   +----+----+
   | 23 | 33 |
   +----+----+
   | 24 | 34 |
   +----+----+
   | 25 | 35 |
   +----+----+


The pagination support is available across all pyexcel plugins.

.. note::

   No column pagination support for query sets as data source. 


*Formatting while transcoding a big data file*

If you are transcoding a big data set, conventional formatting method would not
help unless a on-demand free RAM is available. However, there is a way to minimize
the memory footprint of pyexcel while the formatting is performed.

Let's continue from previous example. Suppose we want to transcode "your_file.csv"
to "your_file.xls" but increase each element by 1.

What we can do is to define a row renderer function as the following:

   >>> def increment_by_one(row):
   ...     for element in row:
   ...         yield element + 1

Then pass it onto save_as function using row_renderer:

   >>> pe.isave_as(file_name="your_file.csv",
   ...             row_renderer=increment_by_one,
   ...             dest_file_name="your_file.xlsx")


.. note::

   If the data content is from a generator, isave_as has to be used.

We can verify if it was done correctly:

   >>> pe.get_sheet(file_name="your_file.xlsx")
   your_file.csv:
   +---+----+----+
   | 2 | 22 | 32 |
   +---+----+----+
   | 3 | 23 | 33 |
   +---+----+----+
   | 4 | 24 | 34 |
   +---+----+----+
   | 5 | 25 | 35 |
   +---+----+----+
   | 6 | 26 | 36 |
   +---+----+----+
   | 7 | 27 | 37 |
   +---+----+----+

.. testcode::
   :hide:

    >>> import os
    >>> os.unlink("your_file.csv")
    >>> os.unlink("your_file.xlsx")

"""  # flake8: noqa
