ifeq ($(shell echo ${AL_PACINO_HOME}),)
$(error Environment variable AL_PACINO_HOME not defined. Please run "source environment" in the repo root directory before running make commands)
endif

