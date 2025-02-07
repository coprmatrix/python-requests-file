#
# spec file for package python-requests-file
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-requests-file
Version:        2.1.0
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/dashea/requests-file
Source:         requests_file-%{version}.tar.gz
Patch1: 35.patch

BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Requests-File
=============

Requests-File is a transport adapter for use with the `Requests`_ Python
library to allow local filesystem access via file:\/\/ URLs.

To use:

.. code-block:: python

    import requests
    from requests_file import FileAdapter

    s = requests.Session()
    s.mount('file://', FileAdapter())

    resp = s.get('file:///path/to/file')

Features
--------

- Will open and read local files
- Might set a Content-Length header
- That's about it

No encoding information is set in the response object, so be careful using
Response.text: the chardet library will be used to convert the file to a
unicode type and it may not detect what you actually want.

EACCES is converted to a 403 status code, and ENOENT is converted to a
404. All other IOError types are converted to a 400.

Contributing
------------

Contributions welcome! Feel free to open a pull request against
https://github.com/dashea/requests-file

License
-------

To maximise compatibility with Requests, this code is licensed under the Apache
license. See LICENSE for more details.

.. _`Requests`: https://github.com/kennethreitz/requests


%prep
%autosetup -p1 -n requests_file-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%{python_sitelib}/requests_file.py
%pycache_only %{python_sitelib}/__pycache__/requests_file.*.py*

%license LICENSE
%doc README.rst
%{python_sitelib}/requests_file-%{version}.dist-info

%changelog
