%global tl_name linop
%global tl_revision 41304

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Typeset linear operators as they appear in quantum theory or linear algebra
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/linop
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linop.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linop.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package aims to provide two simple commands and many options
to easily write linear operators as they appear in many-body physics,
quantum theory, and linear algebra, in any of the ways commonly in use.

