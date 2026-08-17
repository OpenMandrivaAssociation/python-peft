Name:		python-peft
Version:	0.20.0
Release:	1
Summary:	Parameter-Efficient Fine-Tuning of large language models
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/huggingface/peft
Source0:	https://files.pythonhosted.org/packages/source/p/peft/peft-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
PEFT methods enable efficient adaptation of large pretrained models
to various downstream applications without fine-tuning all of the
model's parameters (LoRA, prefix-tuning, adapters, ...).

%files
%doc README.md
%license LICENSE
%{py_sitedir}/peft
%{py_sitedir}/peft-*.*-info
