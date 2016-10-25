Name:           cppo
Version:        1.4.0
Release:        1%{?dist}
Summary:        Equivalent of the C preprocessor for OCaml
License:        BSD3
URL:            http://mjambon.com/cppo.html
Source0:        https://github.com/mjambon/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Equivalent of the C preprocessor for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup

%build
make

%install
%__install -D cppo %{buildroot}/%{_bindir}/cppo
%__install -d %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install META  %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.cmi   %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.cma   %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.cmxa  %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.a     %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.cmxs  %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild
%__install ocamlbuild_plugin/_build/ocamlbuild_cppo.mli   %{buildroot}/%{_libdir}/ocaml/cppo_ocamlbuild

%files
%doc LICENSE 
%doc README.md
%{_bindir}/cppo
%{_libdir}/ocaml/cppo_ocamlbuild
%exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.a
%exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.cmxa
%exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.cmxs
%exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.mli
# these might appear in future releases
# %exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.annot
# %exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.cmt
# %exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.cmti
# %exclude %{_libdir}/ocaml/cppo_ocamlbuild/*.cmx

%files devel
%{_libdir}/ocaml/cppo_ocamlbuild/*.a
%{_libdir}/ocaml/cppo_ocamlbuild/*.cmxa
%{_libdir}/ocaml/cppo_ocamlbuild/*.cmxs
%{_libdir}/ocaml/cppo_ocamlbuild/*.mli
# these might appear in future releases
# %{_libdir}/ocaml/cppo_ocamlbuild/*.cmx

%changelog
* Mon Oct 24 2016 Marcello Seri <marcello.seri@citrix.com> - 1.4.0-1
- Use latest cppo version

* Tue Oct 21 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Switch to GitHub sources

* Fri May 31 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Initial package

