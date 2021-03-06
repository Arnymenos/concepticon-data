# coding: utf8
from __future__ import unicode_literals

import attr


TAGS = {
    "acquisition": "Concept lists related to studies on language acquisition",
    "annotated": "Concept lists which contain further annotations which exceed the "
                 "complexity of ranks",
    "areal": "Concept lists designed for a specific linguistic area.",
    "basic": "Concept lists which are supposed to represent the basic vocabulary.",
    "documentation": "Concept lists which serve to document one language or one language "
                     "family.",
    "hihi": "A list of highly reconstructable and highly retentive items (term from "
            "McMahon & McMahon 2005).",
    "historical": "A list which is historically interesting, mostly referring to lists "
                  "published before the 20th century.",
    "lolo": "A list of less stable basic items, with low reconstructability and low "
            "retentiveness (term from McMahon & McMahon 2005).",
    "naming test": "A list designed for a naming test in neurology or psycholinguistics "
                   "to asses the linguistic capability of children and adults.",
    "proto-language": "A list illustrating the concepts in a proto-language which can be "
                      "reconstructed with high certainty.",
    "questionnaire": "A questionnaire for linguistic field work.",
    "ranked": "A list that shows items in a ranked order, and has one column reflecting "
              "the rank.",
    "sign language": "A list which was designed to investigate sign languages.",
    "specific": "A list that we deem specific, since it is not easy to compare with "
                "other lists in our sample.",
    "stable": "A list that is supposed to represent the stable part of a larger list. "
              "Usually, the stable part has an unstable counterpart.",
    "ultra-stable": "A usually very short list of the supposedly most stable concepts.",
    "unstable": "A list that is supposed to represent the unstable part of a larger "
                "list. Usually has a stable counterpart.",
}

SEMANTICFIELD = {
    "Agriculture and vegetation",
    "Animals",
    "Basic actions and technology",
    "Clothing and grooming",
    "Cognition",
    "Emotions and values",
    "Food and drink",
    "Kinship",
    "Law",
    "Miscellaneous function words",
    "Modern world",
    "Motion",
    "Possession",
    "Quantity",
    "Religion and belief",
    "Sense perception",
    "Social and political relations",
    "Spatial relations",
    "Speech and language",
    "The body",
    "The house",
    "The physical world",
    "Time",
    "Warfare and hunting",
}

ONTOLOGICAL_CATEGORY = {
    "Action/Process",
    "Person/Thing",
    "Classifier",
    "Property",
    "Other",
}


@attr.s
class Languoid(object):
    glottocode = attr.ib()


COLUMN_TYPES = {
    "SUBLIST": "link",
    "URL": "url",
    "PART_OF_SPEECH": "string",
    "ENGLISH": Languoid('stan1293'),
    "SPANISH": Languoid("stan1288"),
    "FRENCH": Languoid("stan1290"),
    "GERMAN": Languoid("stan1295"),
    "RUSSIAN": Languoid("russ1263"),
    "CHINESE": Languoid("mand1415"),
    "LATIN": Languoid("lati1261"),
    "BASQUE": Languoid("basq1248"),
    "ESPERANTO": Languoid("espe1235"),
    "SWEDISH": Languoid("swed1254"),
    "SIKUANI": Languoid("guah1255"),
    "PROTOWORLD": Languoid(None),
    "PROTO_INDO_EUROPEAN": Languoid(None),
    "DUTCH": Languoid("dutc1256"),
    "TURKISH": Languoid("nucl1301"),
    "HAUSA": Languoid("haus1257"),
    "JAPANESE": Languoid("nucl1643"),
    "PORTUGUESE": Languoid('port1283'),
    "FREQUENCY": "int or float",
    "RANK": "int",
    "*SCORE": "int or float"
}
