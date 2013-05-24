#How to use grunt.js to build your application

## What is Grunt?
### [http://gruntjs.com/](http://gruntjs.com/ "grunt 首页")  

	Latest Version 
	Stable: v0.4.1 (2013-05-17)
	
## Why use Grunt?

### Why use a task runner?

> In one word: automation. The less work you have to do when performing repetitive tasks like minification, compilation, unit testing, linting, etc, the easier your job becomes. After you've configured it, a task runner can do most of that mundane work for you—and your team—with basically zero effort.
 
> （一句话：自动化。在一些常规工作，比如：压缩、合并、单元测试、代码检测等上所花费的时间越少，那么你的工作就会更有效率，更能快速产出结果。只要稍微做一些配置，这个任务运行器就可以帮你做很多需要之前人工做的事情。）

来自官网的理由：  
> The Grunt ecosystem is huge and it's growing every day. With literally hundreds of plugins to choose from, you can use Grunt to automate just about anything with a minimum of effort. If someone hasn't already built what you need, authoring and publishing your own Grunt plugin to npm is a breeze. 
 
> （Grunt的生态系统是巨大的而且每天都在快速发展。这里有成千上百个插件供你使用，你只需要一点点努力就可以几乎将所有事情都自动化起来。如果在这个系统里没有你所想要的插件，你还可以通过 npm 将你自己写的插件发布到 Grunt 这个系统中来，供他人使用）

来自我的理由：  		
之前前端资源的文件合并、压缩、部署之类的，都需要借用外部后台语言，如`Ant`等，像我们目前所用的就是`Ant`，并且大家都对里面的实现是什么样的并不清楚，而且如果要做一些改动来满足自己团队的需求，对于前端工程师来说就比较痛苦，需要掌握`Ant`，并学会去改它的配置文件：`Minify/build.xml`，自从有了`Nodejs`后，我们发现前端工程师也可以做一些后端才能做的事情了，而且对于前端来说，`Nodejs`本身就是`js`语言，所以上手很快，前端工程师借助`Nodejs`自己就可以开发一些自动化工具，而不需要再去学习其他的语言，不再依赖于后端。

## Getting Started

### 第一个坑-版本问题
之前很早，在`Grunt 0.3`版本的时候自己就已经尝试过使用`Grunt`来构建项目，并在开发机上部署了环境，跑了起来，但是上周本来满心欢喜的想再重新跑下`Grunt`，结果它跟我说：

![alt text](http://s6.mogujie.cn/pic/130517/2r6z_kqywcmcfnjbgu2cugfjeg5sckzsew_641x77.jpg "Title")

然后`ll`了一下：

![alt text](http://s4.mogujie.cn/pic/130517/2r6z_kqyuet3injbgossugfjeg5sckzsew_420x41.jpg "Title")

是有这个文件的，那到底是什么原因，好吧，既然它提示我们去官网，那就去看下吧：

![alt text](http://s6.mogujie.cn/pic/130517/2r6z_kqywsnsdnjbfiq3wgfjeg5sckzsew_759x252.jpg "Title")

发现，原来在 0.3 版本的时候，是通过 `grunt.js` 这个文件来启动的，到 0.4 版本的时候改成了 `Gruntfile.js`，然后把｀grunt.js` 改成 `Gruntfile.js` 就好了。

#### 总结：  

* 需要仔细查看提示的错误信息，成熟的开源软件在错误提示上做的都是比较好的，程序运行报的错误，只要按照它提示的建议去做，基本都能完成。
* 了解和使用一个东西前，先去它的官网，通过阅读它的文档，了解它。













