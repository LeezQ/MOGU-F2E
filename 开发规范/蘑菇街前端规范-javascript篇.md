# 蘑菇街前端开发规范 - javascript 篇 

- author @mogu_f2e
- create 2013-01-08  

该文档定义了蘑菇街前端团队开发中 javascript 的规范，请参与前端开发的成员务必严格按照规范。该规范包含 4 部分，包括代码风格，javascript 语言规范，组件开发规范，文件命名规范。  

## 代码风格  
> 良好的代码风格和代码风格的一致性是保证团队高效开发的前提，也是作为一支专业团队所必须具备的素质。  

- ### 缩进  
how: 使用4个空格作为缩进方式，请将编辑器 tab 键为空格代替  
why: 由于不同的编辑器对 tab 的显示不一致，为避免代码格式错乱，所以需统一设定。  

- ### 变量命名风格  
how: 使用驼峰命名方式  
why: getValue(驼峰命名) 和 get_value (下划线分割) 的不同地方是驼峰命名可以少一个字符。：）  

        // 类名：首字母大写，名词
        ClassDefine 

        // 方法名：使用动词，或动名词结合，驼峰
        defineFunctionName 

        // 变量名：与方法名类似，驼峰，对某些类型变量使用不同标识。
        commonVariable // 普通变量
        isBoolVariable // bool 类型变量，使用 is 开头
        _privateVariable // 私有变量，使用 _ 开头
        STATIC_VARIABLE // 常量，字母全部大写，中间使用 _ 分隔
### Other Tips:   

        // 多个变量命名，',' 跟在变量名后。（推荐）
        var firstVari = 0,
            secondVari = 1;

        // 不建议写成以下格式，虽然在一些nodejs项目中你可能看到这样。（不推荐！）
        var firstVari = 0
            ,secondVari = 1;

        // 另外不建议将右边赋值对齐。（不推荐！）
        var fristVari       = 0;
        var secondLongVari  = 1;

- ### 代码格式  
how: 可参见 [google c++ code guide](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Formatting)  
why: 统一的代码格式是作为一名专业程序员的首要素质，对代码风格，需要严格控制，而代码层面的规范，基本都是相通的。  

        1、每行代码长度
            每行长度最长 100 字符，若对长度没概念，可设定编辑器屏幕显示区域来达到控制目的。
        
        2、空格使用  
            1）一元操作符前后没有空格，for example:
            i++;
            i--;

            2）二元操作符前后使用一个空格，for example:
            var myName = 'beile';

        3、方法定义
            1）括号前不留空格，')' 后使用一个空格，并紧跟 '{'，多个参数使用 ', ' 隔开，for example:
            function getValue(firstParam, secondParam) {
                // do something ...
            }

        4、条件控制
            1）难以描述，请注意空格使用，for example:
            // if 语句
            if (condition) {
                // do something...
            } else if (condition) {
                // do another thing...
            } else {
                // do something...
            }

            // for 语句
            for (var i = 0; i < 10; i++) {
                // do something...
            }

            // while 语句
            while (condition) {
                // do something...
            }

            // switch 语句
            stitch (condition) {
                case 'case1':
                    // do something...
                case 'case2':
                    // do something...
                default:
                    // do something...
            }
### Other Tips:   
        
        1、如果一行代码太长，请适时断行，for example:
        function theVeryVeryLongMethod(firstLongParams, secondLongParams, thirdLongParams) { // 不推荐！
            // do something... 
        }

        推荐，参数换行：
        function theVeryVeryLongMethod(firstLongParams, 
                                        secondLongParams, // 注意第二个参数的缩进
                                        thirdLongParams) {
            // do something...
        }

        或所有参数另起一行：
        function theVeryVeryLongMethod(
                firstLongParams, // 参数另起一行，注意代码的缩进
                secondLongParams, 
                thirdLongParams) {
            // do something...
        }

        同理，在条件语句中，也需要遵循相同规则。for example:
        if (firstLongCondition 
            || secondLongCondition // 根据运算符另起一行
            || thirdLongCondition) {
            // do something...
        }


## javascript 语言规范  

> 由于 javascript 语言本身的特殊性和所具备的特性，所以在开发 javascript 代码时，我们需要遵循良好的开发规则，从而避免明显的性能问题和一些诡异的 bug。 [什么是 javascript ?](http://zh.wikipedia.org/wiki/JavaScript)  

### 1）永远记得使用 var 定义变量  
how: 定义变量的时候，加上 var 就好了。so easy ~  
why: 若不加 var 变量，则变量的作用域是全局的，会引起一些诡异的 bug。  
        
        var a = 123;
        console.log(a); // 输出 123;
        function bb() {
            a = 234; // 未加 var 定义变量。
        }
        console.log(a); // 输出 234; a 的值变了。

### 2）永远记得使用分号对语句结尾  
how: 在语句结尾的时候，加上';' 就好了，also so easy ~  
why: 虽然浏览器在运行 js 代码时，会在语句结尾自动加上分号，但是不写分号是一个不好的编程习惯，另由于上线时，js 代码会经过压缩，不加分号可能会导致压缩后的代码逻辑与自己所实现的不符。

        var b = 1 // 未加分号结尾
        -1 == 0;
        console.log(b); // 输出为 true; 原因是定义变量 b 时未加分号，导致与下面语句串联后，b 被赋值为 1 - 1;
        所以为避免此种情况发生，请在语句结尾处加上';'

### 3) 创建基本类型时，不要使用 new 基本数据类型的包装对象
why: 使用基本包装对象来创建基本数据类型是完全没有必要的，而且还会影响类型检测和逻辑判断

        var isShow = new Boolean(false);
        console.log(typeof isShow); // 输出 'object'
        if (isShow) { // 此处判断为 true;
            console.log('isShow is true !'); 
        }

        同理，在创建字符串、数值等数据类型时，也不要使用基本数据类型的包装对象。

### 4) 数组、对象的创建
how: 与基本数据类型类似，当你需要使用数组时，不要使用 Array 的构造函数来创建，而是使用数组的数组的直接字面量。
    
        // 使用 Array 构造函数，由于构造函数对参数的处理不够明确，会引起不必要的bug，
        // 例如 new Array(3); 创建的是一个长度为 3 的空数组，而不是创建一个长度为 1、值为 3 的数组。
        // 所以使用直接字面量来创建数组，代码的可读性会更好。也不会给后续埋坑。
        var arr = [1, 2, 3]; // 推荐
        var arr = new Array(1, 2, 3); // 不推荐！

        // 同时推荐使用直接字面量创建对象
        var obj = {}; // 推荐
        var obj = new Object(); // 不推荐！

        创建对象时，对象属性请注意缩进， for example:
        var user = {
            name: 'beile', // 冒号前不留空格，冒号后一个空格
            sex: 'male' // 最后一个属性后不要加 ','，否则在部分浏览器下会报错
        }; // 请不要忘记';' 

### 5) this 对象的使用
how: 在你对 this 对象的指向不明确的时候，请在以下情况中使用 this。
    
        // 在构造函数中
        function People(name) {
            this.name = name;
        }
        // 在构造函数的原型扩展方法中
        People.prototype.showName = function() {
            console.log('my name ' + this.name);
        }

        // 另外如果使用的开发框架是 jQuery，推荐将事件触发的 dom 对象赋值给一个临时变量。for example:
        $('.selector').click(function() {
            var self = $(this); // 可避免在后续的方法中 $(this) 对象的指向不明。
        });

### 6) 避免使用的方法
how: 尽可能不用 eval、with  
why: please tell me why ...囧

### 7) 避免扩展内置对象的原型
why: 对内置对象的扩展，会导致所创建的对象上都会有该属性。

        对内置对象扩展，一个是内存的浪费，一个是在做某些逻辑判断时会导致问题，for example:
        Object.prototype.name = 'hello'; // 在 Object 上扩展原型 name
        var b = {age: 18}; // 创建一个对象
        for(var n in b) { // 遍历 b 中属性
            console.log(n); // 输出 name 、 age
        }

        由于扩展了 Object 对象，所以会输出 name 和 age，当然你也可以通过以下代码避免出错：
        for(var n in b) {
            if(b.hasOwnProperty(n)) {
                console.log(n); 只输出 age
            }
        }

        但是还是需要记住的是，不要在原生对象上扩展原型。
        推荐将方法定义到一个全局对象上来扩展 javascript 所没有的方法，for example：
        mx.util.string.getByte = function(str) {
            // do something...
        }

### 8) 大字符串的创建方式
how: 通过数组来创建大字符串

        不推荐使用 '+' 来拼接大字符串，for example: 
        var listHtml = '<ul class="all_item">' + 
                            '<li class="item">first item</li>' + 
                            '<li class="item">second item</li>' + 
                        '</ul>';

        通过使用数组来创建大字符串是更好的方式，for example:
        var listHtml = [
            '<ul class="all_item">',
                '<li class="item">first item</li>',
                '<li class="item">second item</li>',
            '</ul>'
        ].join(''); // 使用 jion 拼接


## 组件开发规范  
### 1）使用闭包来封装代码块 
how: 通过使用 var 声明变量和闭包的结合，可以有效控制代码块的作用域，从而避免暴露到全局中。  
        
        for example:
        (function($, Mx) {
            var fruit = 'banner';
        })(jQuery, Mx); // 虽然 jQuery 是全局变量，但最好在闭包中显式声明参数，这样可以方便知道该组件使用了哪些框架。另：最后不要忘了';'

### 2) 代码注释
how: 遵循一定的规范，最重要的一点，不要怕注释多！
        
        1、文件头部注释：
        包含版权信息或开源协议等，不做强制要求。for example:
        //
        // Licensed under the Apache License, Version 2.0 (the "License");
        // you may not use this file except in compliance with the License.
        // You may obtain a copy of the License at
        //
        //      http://www.apache.org/licenses/LICENSE-2.0
        //

        2、自定义 Class 注释：（可以使用多个 * 将注释包裹）for example:
        /************************************************ 
        *
        * 类的功能介绍，简述类的使用方法和功能。
        * @require: a.js
        *           b.js // 依赖的 js 文件
        * @author: 作者
        * @create: 创建时间
        * @modify: 最后修改时间，对于通用组件不做强制要求。但是对于业务代码，每次修改需写明负责人和时间。
        * 
        *************************************************

        3、方法的注释 for example: 
        /**
         * 方法的功能介绍
         * @param: {string} str
         *          {object} options // 指明参数的类型
         * @return: {string} str // 返回类型
         * @author: 作者
         * @create: 创建时间
         * @modify: 最后修改时间
         */

### 3）类构造方式
        
        (function() {
            // 首先定义构造函数，
            function MyClass(options) { // 参数可选
                this.option = options;
            }

            // 通过原型扩展类
            MyClass.prototype.method = function(params) { 
                // do something...
            }
        });

        // 通过使用 new 来创建自定义类的实例
        var myFirstClass = new MyClass({name: 'beile'});
        

#### Some Tips

        
        为什么使用原型扩展类？
        通过使用原型扩展类，在新建类的时候，只有类构造参数中的属性或方法是独立的内存，而原型上的方法的内存是共用的。

        如果你想自定义类的某个方法，若不是全局的改动，直接使用覆盖新建对象的方式来达到个性化的目的，for example:
        myFirstCLass.method = function(params) {
            // do another thing...
        }
        而不要直接修改类的原型来达到目的，
        MyClass.prototype.method = function(params) { // 不推荐！除非你的所有对象实例都需要修改这个方法。
            // do something...
        }

        建议在构造函数中只是定义类的属性，不要添加逻辑代码，以免业务变化时，不能很好的适应需求。for example: 
        // 在类中加了一段逻辑代码
        function MyClass(options) { // 参数可选
            this.option = options;
            var myLogic = this.option.logic;
            if (myLogic == 0) {
                // do something...
            }
        }
        这样，每次新建一个对象实例时，都会走这段逻辑。当我某个业务中不需要走 myLogic == 0 时，处理就会很麻烦。
        推荐将初始逻辑代码放到一个 init 函数中。


### 4) 类继承

    // todo

## 文件组织规范  
    // todo ..

## javascript 代码技巧参考示例
    // todo ..