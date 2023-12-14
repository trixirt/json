# For testing
# Depends on downloading and being in a git repo
%bcond_with test

# Header only package
%global debug_package %{nil}

Summary:        JSON for Modern C++
Name:           nlohmann_json
License:        MIT AND BSD-3-Clause AND Apache-2.0 AND GPL-3.0-only
Version:        3.11.3
Release:        1%{?dist}

URL:            https://github.com/nlohmann/json
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/json-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
There are myriads of JSON libraries out there, and each may even
have its reason to exist. Our class had these design goals:

Intuitive syntax. In languages such as Python, JSON feels like a
first class data type. We used all the operator magic of modern
C++ to achieve the same feeling in your code. Check out the
examples and you'll know what I mean.

Trivial integration. Our whole code consists of a single header
file json.hpp. That's it. No library, no subproject, no
dependencies, no complex build system. The class is written in
vanilla C++11. All in all, everything should require no adjustment
of your compiler flags or project settings.

Serious testing. Our code is heavily unit-tested and covers 100% of
the code, including all exceptional behavior. Furthermore, we checked
with Valgrind and the Clang Sanitizers that there are no memory leaks.
Google OSS-Fuzz additionally runs fuzz tests against all parsers 24/7,
effectively executing billions of tests so far. To maintain high
quality, the project is following the Core Infrastructure Initiative
(CII) best practices.

%package devel

Summary:        JSON for Modern C++
Provides:       %{name}-static = %{version}-%{release}

%description devel
There are myriads of JSON libraries out there, and each may even
have its reason to exist. Our class had these design goals:

Intuitive syntax. In languages such as Python, JSON feels like a
first class data type. We used all the operator magic of modern
C++ to achieve the same feeling in your code. Check out the
examples and you'll know what I mean.

Trivial integration. Our whole code consists of a single header
file json.hpp. That's it. No library, no subproject, no
dependencies, no complex build system. The class is written in
vanilla C++11. All in all, everything should require no adjustment
of your compiler flags or project settings.

Serious testing. Our code is heavily unit-tested and covers 100% of
the code, including all exceptional behavior. Furthermore, we checked
with Valgrind and the Clang Sanitizers that there are no memory leaks.
Google OSS-Fuzz additionally runs fuzz tests against all parsers 24/7,
effectively executing billions of tests so far. To maintain high
quality, the project is following the Core Infrastructure Initiative
(CII) best practices.

%prep
%autosetup -p1 -n json-%{version}

%build
%cmake -DCMAKE_INSTALL_DATADIR=%{_libdir}
%cmake_build

%if %{with test}
# The expected results
# The following tests FAILED:
# 88 - cmake_fetch_content_configure (Failed)
# 89 - cmake_fetch_content_build (Not Run)
# 90 - cmake_fetch_content2_configure (Failed)
# 91 - cmake_fetch_content2_build (Not Run)
%check
%ctest
%endif

%install
%cmake_install

%files devel
%license LICENSE.MIT
%license LICENSES/
%doc README.md
%_includedir/nlohmann/
%_libdir/cmake/%{name}/
%_libdir/pkgconfig/%{name}.pc


%changelog
* Thu Dec 14 2023 Tom Rix <trix@redhat.com> - 3.11.3-1
- Initial package
