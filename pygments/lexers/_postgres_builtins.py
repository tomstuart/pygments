"""
    pygments.lexers._postgres_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Self-updating data files for PostgreSQL lexer.

    :copyright: Copyright 2011 by Daniele Varrazzo.
    :license: BSD, see LICENSE for details.
"""

import re
import urllib2

# One man's constant is another man's variable.
SOURCE_URL = 'https://github.com/postgres/postgres/raw/master'
KEYWORDS_URL = SOURCE_URL + '/doc/src/sgml/keywords.sgml'
DATATYPES_URL = SOURCE_URL + '/doc/src/sgml/datatype.sgml'

def update_myself():
    datatypes = parse_datatypes(fetch(DATATYPES_URL))
    keywords = parse_keywords(fetch(KEYWORDS_URL))
    update_consts(__file__, 'DATATYPES', datatypes)
    update_consts(__file__, 'KEYWORDS', keywords)

def parse_keywords(f):
    kw = []
    for m in re.finditer(
            r'\s*<entry><token>([^<]+)</token></entry>\s*'
            r'<entry>([^<]+)</entry>', f.read()):
        kw.append(m.group(1))

    if not kw:
        raise ValueError('no keyword found')

    kw.sort()
    return kw

def parse_datatypes(f):
    dt = set()
    re_entry = re.compile('\s*<entry><type>([^<]+)</type></entry>')
    for line in f:
        if '<sect1' in line:
            break
        if '<entry><type>' not in line:
            continue

        # Parse a string such as
        # time [ (<replaceable>p</replaceable>) ] [ without time zone ]
        # into types "time" and "without time zone"

        # remove all the tags
        line = re.sub("<replaceable>[^<]+</replaceable>", "", line)
        line = re.sub("<[^>]+>", "", line)

        # Drop the parts containing braces
        for tmp in [ t for tmp in line.split('[') for t in tmp.split(']') if "(" not in t ]:
            for t in tmp.split(','):
                t = t.strip()
                if not t: continue
                dt.add(" ".join(t.split()))

    dt = list(dt)
    dt.sort()
    return dt

def fetch(url):
    return urllib2.urlopen(url)

def update_consts(filename, constname, content):
    f = open(filename)
    lines = f.readlines()
    f.close()

    # Line to start/end inserting
    re_start = re.compile(r'^%s\s*=\s*\[\s*$' % constname)
    re_end = re.compile(r'^\s*\]\s*$')
    start = [ n for n, l in enumerate(lines) if re_start.match(l) ]
    if not start:
        raise ValueError("couldn't find line containing '%s = ['" % constname)
    if len(start) > 1:
        raise ValueError("too many lines containing '%s = ['" % constname)
    start = start[0] + 1

    end = [ n for n, l in enumerate(lines) if n >= start and re_end.match(l) ]
    if not end:
        raise ValueError("couldn't find line containing ']' after %s " % constname)
    end = end[0]

    # Pack the new content in lines not too long
    content = [repr(item) for item in content ]
    new_lines = [[]]
    for item in content:
        if sum(map(len, new_lines[-1])) + 2 * len(new_lines[-1]) + len(item) + 4 > 75:
            new_lines.append([])
        new_lines[-1].append(item)

    lines[start:end] = [ "    %s,\n" % ", ".join(items) for items in new_lines ]

    f = open(filename, 'w')
    f.write(''.join(lines))
    f.close()


# Autogenerated: please edit them if you like wasting your time.

KEYWORDS = [
    'ABORT', 'ABSOLUTE', 'ACCESS', 'ACTION', 'ADD', 'ADMIN', 'AFTER',
    'AGGREGATE', 'ALL', 'ALSO', 'ALTER', 'ALWAYS', 'ANALYSE', 'ANALYZE',
    'AND', 'ANY', 'ARRAY', 'AS', 'ASC', 'ASSERTION', 'ASSIGNMENT',
    'ASYMMETRIC', 'AT', 'ATTRIBUTE', 'AUTHORIZATION', 'BACKWARD', 'BEFORE',
    'BEGIN', 'BETWEEN', 'BIGINT', 'BINARY', 'BIT', 'BOOLEAN', 'BOTH', 'BY',
    'CACHE', 'CALLED', 'CASCADE', 'CASCADED', 'CASE', 'CAST', 'CATALOG',
    'CHAIN', 'CHAR', 'CHARACTER', 'CHARACTERISTICS', 'CHECK', 'CHECKPOINT',
    'CLASS', 'CLOSE', 'CLUSTER', 'COALESCE', 'COLLATE', 'COLLATION',
    'COLUMN', 'COMMENT', 'COMMENTS', 'COMMIT', 'COMMITTED', 'CONCURRENTLY',
    'CONFIGURATION', 'CONNECTION', 'CONSTRAINT', 'CONSTRAINTS', 'CONTENT',
    'CONTINUE', 'CONVERSION', 'COPY', 'COST', 'CREATE', 'CROSS', 'CSV',
    'CURRENT', 'CURRENT_CATALOG', 'CURRENT_DATE', 'CURRENT_ROLE',
    'CURRENT_SCHEMA', 'CURRENT_TIME', 'CURRENT_TIMESTAMP', 'CURRENT_USER',
    'CURSOR', 'CYCLE', 'DATA', 'DATABASE', 'DAY', 'DEALLOCATE', 'DEC',
    'DECIMAL', 'DECLARE', 'DEFAULT', 'DEFAULTS', 'DEFERRABLE', 'DEFERRED',
    'DEFINER', 'DELETE', 'DELIMITER', 'DELIMITERS', 'DESC', 'DICTIONARY',
    'DISABLE', 'DISCARD', 'DISTINCT', 'DO', 'DOCUMENT', 'DOMAIN', 'DOUBLE',
    'DROP', 'EACH', 'ELSE', 'ENABLE', 'ENCODING', 'ENCRYPTED', 'END',
    'ENUM', 'ESCAPE', 'EXCEPT', 'EXCLUDE', 'EXCLUDING', 'EXCLUSIVE',
    'EXECUTE', 'EXISTS', 'EXPLAIN', 'EXTENSION', 'EXTERNAL', 'EXTRACT',
    'FALSE', 'FAMILY', 'FETCH', 'FIRST', 'FLOAT', 'FOLLOWING', 'FOR',
    'FORCE', 'FOREIGN', 'FORWARD', 'FREEZE', 'FROM', 'FULL', 'FUNCTION',
    'FUNCTIONS', 'GLOBAL', 'GRANT', 'GRANTED', 'GREATEST', 'GROUP',
    'HANDLER', 'HAVING', 'HEADER', 'HOLD', 'HOUR', 'IDENTITY', 'IF',
    'ILIKE', 'IMMEDIATE', 'IMMUTABLE', 'IMPLICIT', 'IN', 'INCLUDING',
    'INCREMENT', 'INDEX', 'INDEXES', 'INHERIT', 'INHERITS', 'INITIALLY',
    'INLINE', 'INNER', 'INOUT', 'INPUT', 'INSENSITIVE', 'INSERT', 'INSTEAD',
    'INT', 'INTEGER', 'INTERSECT', 'INTERVAL', 'INTO', 'INVOKER', 'IS',
    'ISNULL', 'ISOLATION', 'JOIN', 'KEY', 'LABEL', 'LANGUAGE', 'LARGE',
    'LAST', 'LC_COLLATE', 'LC_CTYPE', 'LEADING', 'LEAST', 'LEFT', 'LEVEL',
    'LIKE', 'LIMIT', 'LISTEN', 'LOAD', 'LOCAL', 'LOCALTIME',
    'LOCALTIMESTAMP', 'LOCATION', 'LOCK', 'MAPPING', 'MATCH', 'MAXVALUE',
    'MINUTE', 'MINVALUE', 'MODE', 'MONTH', 'MOVE', 'NAME', 'NAMES',
    'NATIONAL', 'NATURAL', 'NCHAR', 'NEXT', 'NO', 'NONE', 'NOT', 'NOTHING',
    'NOTIFY', 'NOTNULL', 'NOWAIT', 'NULL', 'NULLIF', 'NULLS', 'NUMERIC',
    'OBJECT', 'OF', 'OFF', 'OFFSET', 'OIDS', 'ON', 'ONLY', 'OPERATOR',
    'OPTION', 'OPTIONS', 'OR', 'ORDER', 'OUT', 'OUTER', 'OVER', 'OVERLAPS',
    'OVERLAY', 'OWNED', 'OWNER', 'PARSER', 'PARTIAL', 'PARTITION',
    'PASSING', 'PASSWORD', 'PLACING', 'PLANS', 'POSITION', 'PRECEDING',
    'PRECISION', 'PREPARE', 'PREPARED', 'PRESERVE', 'PRIMARY', 'PRIOR',
    'PRIVILEGES', 'PROCEDURAL', 'PROCEDURE', 'QUOTE', 'RANGE', 'READ',
    'REAL', 'REASSIGN', 'RECHECK', 'RECURSIVE', 'REF', 'REFERENCES',
    'REINDEX', 'RELATIVE', 'RELEASE', 'RENAME', 'REPEATABLE', 'REPLACE',
    'REPLICA', 'RESET', 'RESTART', 'RESTRICT', 'RETURNING', 'RETURNS',
    'REVOKE', 'RIGHT', 'ROLE', 'ROLLBACK', 'ROW', 'ROWS', 'RULE',
    'SAVEPOINT', 'SCHEMA', 'SCROLL', 'SEARCH', 'SECOND', 'SECURITY',
    'SELECT', 'SEQUENCE', 'SEQUENCES', 'SERIALIZABLE', 'SERVER', 'SESSION',
    'SESSION_USER', 'SET', 'SETOF', 'SHARE', 'SHOW', 'SIMILAR', 'SIMPLE',
    'SMALLINT', 'SOME', 'STABLE', 'STANDALONE', 'START', 'STATEMENT',
    'STATISTICS', 'STDIN', 'STDOUT', 'STORAGE', 'STRICT', 'STRIP',
    'SUBSTRING', 'SYMMETRIC', 'SYSID', 'SYSTEM', 'TABLE', 'TABLES',
    'TABLESPACE', 'TEMP', 'TEMPLATE', 'TEMPORARY', 'TEXT', 'THEN', 'TIME',
    'TIMESTAMP', 'TO', 'TRAILING', 'TRANSACTION', 'TREAT', 'TRIGGER',
    'TRIM', 'TRUE', 'TRUNCATE', 'TRUSTED', 'TYPE', 'UNBOUNDED',
    'UNCOMMITTED', 'UNENCRYPTED', 'UNION', 'UNIQUE', 'UNKNOWN', 'UNLISTEN',
    'UNLOGGED', 'UNTIL', 'UPDATE', 'USER', 'USING', 'VACUUM', 'VALID',
    'VALIDATE', 'VALIDATOR', 'VALUE', 'VALUES', 'VARCHAR', 'VARIADIC',
    'VARYING', 'VERBOSE', 'VERSION', 'VIEW', 'VOLATILE', 'WHEN', 'WHERE',
    'WHITESPACE', 'WINDOW', 'WITH', 'WITHOUT', 'WORK', 'WRAPPER', 'WRITE',
    'XML', 'XMLATTRIBUTES', 'XMLCONCAT', 'XMLELEMENT', 'XMLEXISTS',
    'XMLFOREST', 'XMLPARSE', 'XMLPI', 'XMLROOT', 'XMLSERIALIZE', 'YEAR',
    'YES', 'ZONE',
    ]

DATATYPES = [
    'bigint', 'bigserial', 'bit', 'bit varying', 'bool', 'boolean', 'box',
    'bytea', 'char', 'character', 'character varying', 'cidr', 'circle',
    'date', 'decimal', 'double precision', 'float4', 'float8', 'inet',
    'int', 'int2', 'int4', 'int8', 'integer', 'interval', 'line', 'lseg',
    'macaddr', 'money', 'numeric', 'path', 'point', 'polygon', 'real',
    'serial', 'serial4', 'serial8', 'smallint', 'text', 'time', 'timestamp',
    'timestamptz', 'timetz', 'tsquery', 'tsvector', 'txid_snapshot', 'uuid',
    'varbit', 'varchar', 'with time zone', 'without time zone', 'xml',
    ]


if __name__ == '__main__':
    update_myself()

