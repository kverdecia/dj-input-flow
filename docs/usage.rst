=====
Usage
=====

To use dj-input-flow in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'inputflow.apps.InputFlowConfig',
        ...
    )

Add dj-input-flow's URL patterns:

.. code-block:: python

    from inputflow import urls as inputflow_urls


    urlpatterns = [
        ...
        url(r'^', include(inputflow_urls)),
        ...
    ]
