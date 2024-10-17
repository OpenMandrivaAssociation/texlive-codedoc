Name:		texlive-codedoc
Version:	17630
Release:	2
Summary:	LaTeX code and documentation in LaTeX-format file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/codedoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codedoc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The CodeDoc class is an alternative to DocStrip (and others) to
produce LaTeX code along with its documentation without
departing from LaTeX's ordinary syntax. The documentation is
prepared like any other LaTeX document and the code to be
commented verbatim is simply delimited by an environment. When
an option is turned on in the class options, this code is
written to the desired file(s). The class also includes fully
customizable verbatim environments which provide the author
with separate commands to typeset the material and/or to
execute it.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/codedoc/codedoc.cls
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.pdf
%doc %{_texmfdistdir}/doc/latex/codedoc/CodeDoc-manual.tex
%doc %{_texmfdistdir}/doc/latex/codedoc/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
