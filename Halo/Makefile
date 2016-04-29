obj-m := ldm.o
$(obj-m:.o=)-objs := Halo.o

KERN_ROOT := /usr/src/linux-headers-3.11.0-15-generic/
#KERN_ROOT :=/home/hanqiwei/driveLinux/linux-3.5/
#KERN_ROOT := /lib/modules/`uname -r`/build/
NFSROOT := /mnt/hostroot

ccflags-y += -Wno-declaration-after-statement

all: build

build:
	make -C $(KERN_ROOT) M=`pwd` modules

mv:
	mv $(obj-m:.o=.ko) $(NFSROOT)

clean:
	make M=`pwd` -C $(KERN_ROOT) clean

.PHONY: all build mv clean
