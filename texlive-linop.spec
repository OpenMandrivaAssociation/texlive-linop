Name:		texlive-linop
Version:	41304
Release:	2
Summary:	Typeset linear operators as they appear in quantum theory or linear algebra
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linop
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linop.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package aims to provide two simple commands and many
options to easily write linear operators as they appear in
many-body physics, quantum theory, and linear algebra, in any
of the ways commonly in use.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/linop
%doc %{_texmfdistdir}/doc/latex/linop

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
