=====
Usage
=====

To use dj-input-flow in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'adminsortable',
        'inputflow',
        ...
    )

Add dj-input-flow's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path('inputflow/', include('inputflow.urls', 'inputflow')),
        ...
    ]
