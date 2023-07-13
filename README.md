<!-- SPDX-FileCopyrightText: Copyright DB Netz AG and contributors
SPDX-License-Identifier: Apache-2.0 -->

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

# Licenses

This project is compliant with the [REUSE Specification Version 3.0](https://git.fsfe.org/reuse/docs/src/commit/d173a27231a36e1a2a3af07421f5e557ae0fec46/spec.md)

Copyright DB Netz AG, licensed under Apache 2.0 (see full text in
[LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt))

Dot-files are licensed under CC0-1.0 (see full text in
[LICENSES/CC0-1.0.txt](LICENSES/Apache-2.0.txt))

All GIF, PNG, JPEG or SVG files in the template are licensed under EPL-2.0 (see full text in
[LICENSES/EPL-2.0.txt](LICENSES/Apache-2.0.txt))
