#include <Python.h>

void print_python_string(PyObject *p) {
    PyUnicodeObject *unicode;
    PyASCIIObject *ascii;
    Py_ssize_t length;
    wchar_t *wide_str;
    char *str;
    int i;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *)p;
    length = PyUnicode_GET_LENGTH(p);
    wide_str = PyUnicode_AsWideCharString(p, &length);
    str = (char *)PyUnicode_AsUTF8(unicode);

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        printf("  type: compact ascii\n");
        printf("  length: %ld\n", length);
        printf("  value: %s\n", str);
    } else {
        printf("  type: compact unicode object\n");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", wide_str);
    }

    PyMem_Free(wide_str);
}
