=======
pywords
=======

This is a python interface for the Words API at <https://www.wordsapi.com/>. You will need an API key from [Mashape](https://mashape.com) in order to interact with this API.

=======
Install
=======

.. code-block:: bash

    pip install pywords

=======
Example
=======

.. code-block:: python

  import os

  import words

  client = words.words.Words(os.environ['MASHAPE_TOKEN'])

  client.random()

  {u'pronunciation': {}, u'word': u'glyphography', u'rhymes': {u'all': u'-\u0251gr\u0259fi'}}

  client.word('soliloquy')

  {u'frequency': 2.24, u'syllables': {u'count': 4, u'list': [u'so', u'lil', u'o', u'quy']}, u'pronunciation': {u'all': u"s\u0259'l\u026al\u0259kwi"}, u'word': u'soliloquy', u'results': [{u'definition': u'speech you make to yourself', u'synonyms': [u'monologue'], u'typeOf': [u'speech', u'voice communication', u'speech communication', u'spoken communication', u'spoken language', u'language', u'oral communication'], u'partOfSpeech': u'noun', u'derivation': [u'soliloquize']}, {u'definition': u'a (usually long) dramatic speech intended to give the illusion of unspoken reflections', u'typeOf': [u"actor's line", u'speech', u'words'], u'partOfSpeech': u'noun', u'derivation': [u'soliloquize']}]}


=======
License
=======

MIT
