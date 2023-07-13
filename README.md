# Polarion DBS Project Template
A Polarion project template with icons and predefined work item types, work
item type links for Capella model objects.

# How to use the template?
In the global administration you can find a ``Project Templates`` tab. There
under ``Custom Templates`` you are able to upload a ZIP file containing the
template. On creation of new projects you should be able to select the uploaded
template.

# Updating the template
This is achieved by the very same routine described under ``How to use the
template``. Take care that on modifying or deleting existing configurations has
critical effects on work items in projects which use this template. Changing
IDs of work item (link) types will corrupt existing work items. They need to be
patched to the corresponding modifications to the configuration. As this can be
a tedious task, it may be wise to do this via a migration script.
