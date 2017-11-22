%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if !%{opt}
%global debug_package %{nil}
%endif

Name:           ocaml-xmlm
Version:        1.2.0
Release:        24%{?dist}
Summary:        A streaming XML codec

License:        BSD
URL:            http://erratique.ch/software/xmlm
Source0:        http://erratique.ch/software/xmlm/releases/xmlm-%{version}.tbz
# Ensure source files are included in generated debuginfo subpackage
Patch0:         xmlm-1.2.0-debug.patch
# Example XML files for testing
Source1:        test-valid.xml
Source2:        test-invalid.xml

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib

%global libname %(sed -e 's/^ocaml-//' <<< %{name})

%description
Xmlm is an OCaml streaming codec to decode and encode the XML data
format. It can process XML documents without a complete in-memory
representation of the data.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{libname}-%{version}
%patch0 -p1 -b .debug


%build
%if %{opt}
./pkg/build true
%else
./pkg/build false
%endif


%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $OCAMLFIND_DESTDIR/%{libname}

%if %{opt}
install -m 755 -p _build/test/xmltrip.native $RPM_BUILD_ROOT%{_bindir}/xmltrip
install -m 644 -p _build/src/xmlm.{a,cmxa} $OCAMLFIND_DESTDIR/%{libname}/
install -m 755 -p _build/src/xmlm.cmxs $OCAMLFIND_DESTDIR/%{libname}/
%else
install -m 755 -p _build/test/xmltrip.byte $RPM_BUILD_ROOT%{_bindir}/xmltrip
%endif
install -m 644 -p _build/pkg/META _build/src/xmlm.{cm?,mli} $OCAMLFIND_DESTDIR/%{libname}/


%check
# Against valid XML
$RPM_BUILD_ROOT%{_bindir}/xmltrip -p %{SOURCE1} 2>valid-err.log
[ -z "$(cat valid-err.log)" ]

# Against invalid XML - stderr should contain the word expected
$RPM_BUILD_ROOT%{_bindir}/xmltrip -p %{SOURCE2} 2>invalid-err.log
grep expected invalid-err.log >/dev/null

%files
# LICENSE not bundled
%doc README.md
%{_bindir}/xmltrip
%{_libdir}/ocaml/xmlm/
%if %opt
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmxs
%exclude %{_libdir}/ocaml/*/*.cmx
%endif
%exclude %{_libdir}/ocaml/*/*.mli


%files devel
# LICENSE not bundled
%doc CHANGES.md _build/test/examples.ml _build/test/xhtml.ml doc
%if %opt
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli


%changelog
* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-24
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-21
- OCaml 4.04.2 rebuild.

* Sat May 13 2017 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-20
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.2.0-18
- rebuild for s390x codegen bug

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-17
- Rebuild for OCaml 4.04.0.
- Add explicit dependency on ocamlbuild.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-15
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-14
- ocaml-4.02.2 final rebuild.

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-13
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-11
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-10
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-9
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-7
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 1.2.0-6
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jaromir Capik <jcapik@redhat.com> - 1.2.0-4
- Removing ExclusiveArch

* Fri Feb 14 2014 Michel Salim <salimma@fedoraproject.org> - 1.2.0-3
- Include source files in -debuginfo

* Sat Feb  8 2014 Michel Salim <salimma@fedoraproject.org> - 1.2.0-2
- Incorporate review feedback

* Mon Jan 20 2014 Michel Salim <salimma@fedoraproject.org> - 1.2.0-1
- Initial package
