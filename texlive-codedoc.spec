%global tl_name codedoc
%global tl_revision 17630

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	LaTeX code and documentation in LaTeX-format file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codedoc
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The CodeDoc class is an alternative to DocStrip (and others) to produce
LaTeX code along with its documentation without departing from LaTeX's
ordinary syntax. The documentation is prepared like any other LaTeX
document and the code to be commented verbatim is simply delimited by an
environment. When an option is turned on in the class options, this code
is written to the desired file(s). The class also includes fully
customizable verbatim environments which provide the author with
separate commands to typeset the material and/or to execute it.

