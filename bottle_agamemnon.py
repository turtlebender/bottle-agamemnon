import inspect

from agamemnon.factory import load_from_settings
from bottle import PluginError

class AgamemnonPlugin(object):
    """
    This passes a configured Agamemnon data store into any method which has an
    'agadb' parameter.
    """

    def __init__(self, keyword='agadb', backend="agamemnon.memory.InMemoryDataStore", 
            **settings):
        self.settings = settings
        self.settings['backend'] = backend
        self.keyword = keyword
        self.datastore = None

    def setup(self, app):
        """
        Initialize the agamemnon datastore.

        Parameters:
          - app: the application into which this plugin is being loaded.

        Returns: None
        """
        for other in app.plugins:
            if not isinstance(other, AgamemnonPlugin): 
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another agamemnon plugins with "\
                        "same keyword")
        if self.datastore is None:
            self.datastore = load_from_settings(self.settings)

    def apply(self, callback, context):
        """
        If the callback method has a parameter called 'agadb' pass the
        configured datastore into the callback.

        Parameters:
        - callback: The callback function
        - context: The route context of the call.

        Returns: wrapper function.
        """
        conf = context['config'].get('agamemnon') or {}
        args = inspect.getargspec(context['callback'])[0]
        keyword = conf.get('keyword', self.keyword)
        if keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            """
            Call method with agamemnon datastore injected
            """
            kwargs[self.keyword] = self.datastore
            return callback(*args, **kwargs)
        return wrapper

Plugin = AgamemnonPlugin
