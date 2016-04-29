#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>

static int __init halo_init(void)
{
	printk(KERN_ALERT "Initialization the module ...\n");
	return 0;
}

static void __exit halo_exit(void)
{
	printk(KERN_ALERT "Remove the module!\n");
}

module_init(halo_init);
module_exit(halo_exit);

MODULE_LICENSE("GPL");  
MODULE_DESCRIPTION("Hello,First Android Driver"); 
MODULE_VERSION("Ver 0.1");
