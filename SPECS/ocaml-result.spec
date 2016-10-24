%global debug_package %{nil}

Name:           ocaml-result
Version:        1.2
Release:        2%{?dist}
Summary:        Defines the result type for OCaml < 4.03
License:        BSD
URL:            https://github.com/janestreet/result
Source0:        https://github.com/janestreet/result/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
This library defines the polymorphic result type for OCaml < 4.03.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n result-%{version}

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install DESTDIR=${buildroot}

%files
%doc README.md
%doc LICENSE
%{_libdir}/ocaml/result
%exclude %{_libdir}/ocaml/result/*.o
%exclude %{_libdir}/ocaml/result/*.ml
%exclude %{_libdir}/ocaml/result/*.install
%exclude %{_libdir}/ocaml/result/*.a
%exclude %{_libdir}/ocaml/result/*.cmx
%exclude %{_libdir}/ocaml/result/*.cmxa
%exclude %{_libdir}/ocaml/result/*.cmxs

%files devel
%{_libdir}/ocaml/result/*.a
%{_libdir}/ocaml/result/*.cmx
%{_libdir}/ocaml/result/*.cmxa
%{_libdir}/ocaml/result/*.cmxs

%changelog
* Mon Oct 24 2016 Marcello Seri <marcello.seri@citrix.com> - 1.2-2
- Cleanup content

* Thu Oct 20 2016 Christian Lindig <christian.lindig@citrix.com> - 1.2-1
- Initial packaging.
