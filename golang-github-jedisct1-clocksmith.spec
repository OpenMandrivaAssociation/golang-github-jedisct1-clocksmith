# Run tests in check section
%bcond_without check

%global goipath         github.com/jedisct1/go-clocksmith
%global commit          c35da9bed550558a4797c74e34957071214342e7

%global common_description %{expand:
A sleep-aware sleep() function, that doesn't pause (for too long) if the 
system goes to hibernation.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A sleep-aware-sleep() function 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitc35da9b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180529gitc35da9b
- First package for Fedora

