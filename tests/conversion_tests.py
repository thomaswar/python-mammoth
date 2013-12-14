from nose.tools import istest, assert_equal

from mammoth import documents, style_reader
from mammoth.conversion import convert_document_element_to_html


@istest
def plain_paragraph_is_converted_to_plain_paragraph():
    result = convert_document_element_to_html(
        documents.paragraph(children=[_run_with_text("Hello")])
    )
    assert_equal('<p>Hello</p>', result.value)


@istest
def empty_paragraphs_are_ignored():
    result = convert_document_element_to_html(
        documents.paragraph(children=[_run_with_text("")])
    )
    assert_equal('', result.value)


@istest
def paragraphs_are_converted_by_satisfying_matching_paths():
    result = convert_document_element_to_html(
        documents.paragraph(style_name="TipsParagraph", children=[
            _run_with_text("Tip")
        ]),
        styles=[
            style_reader.read_style("p.TipsParagraph => p.tip")
        ]
    )
    assert_equal('<p class="tip">Tip</p>', result.value)


def _run_with_text(text):
    return documents.run(children=[documents.text(text)])