# 英语注释自动翻译助手

[![license](https://img.shields.io/badge/license-Apache%20License%202.0-brightgreen.svg?style=flat)](https://github.com/murphy-li/Clipboard2Voice/blob/master/LICENSE)<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg"></a>

## 简介

本项目主要用于帮助大家查看源代码时将烦人的英语自动机翻为中文（使用谷歌翻译），暂时只支持Java注释：```/***/```，其他的注释如```//```或者其他语言暂时未兼容。

效果参考如下：
```
/** Generated by english-annotation-buster, Powered by Google Translate.**/
/*
 * Copyright 2002-2016 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * 版权所有2002-2016的原始作者。 
 * 根据Apache许可证2.0版（"许可证"）获得许可； 
 * 除非遵守许可，否则不得使用此文件。 
 * 您可以在https://www.apache.org/licenses/LICENSE-2.0上获得许可的副本。 
 * 除非适用法律要求或以书面形式同意，否则根据"许可"分发的软件将按"现状"分发，没有任何明示或暗示的保证或条件。 
 * 有关许可下特定的语言管理权限和限制，请参阅许可。 
 * 
 */

package org.aopalliance.intercept;

/**
 * Intercepts the construction of a new object.
 *
 * <p>The user should implement the {@link
 * #construct(ConstructorInvocation)} method to modify the original
 * behavior. E.g. the following class implements a singleton
 * interceptor (allows only one unique instance for the intercepted
 * class):
 *
 * <pre class=code>
 * class DebuggingInterceptor implements ConstructorInterceptor {
 *   Object instance=null;
 *
 *   Object construct(ConstructorInvocation i) throws Throwable {
 *     if(instance==null) {
 *       return instance=i.proceed();
 *     } else {
 *       throw new Exception("singleton does not allow multiple instance");
 *     }
 *   }
 * }
 * </pre>
 *
 * @author Rod Johnson
 */
/**
 * 拦截新对象的构造。 
 *  <p>用户应实现{@link  #construct（ConstructorInvocation）}方法以修改原始行为。 
 * 例如。 
 * 以下类实现了单例拦截器（被拦截的类仅允许一个唯一的实例）：<pre class = code>类DebuggingInterceptor实现了ConstructorInterceptor {Object instance = null;对象的construct（ConstructorInvocation i）抛出Throwable {if（instance == null）{return instance = i.proceed（）; } else {抛出新异常（"单个不允许多个实例"））； 
 *  }}} </ pre> @author  Rod Johnson
 */
public interface ConstructorInterceptor extends Interceptor  {

	/**
	 * Implement this method to perform extra treatments before and
	 * after the construction of a new object. Polite implementations
	 * would certainly like to invoke {@link Joinpoint#proceed()}.
	 * @param invocation the construction joinpoint
	 * @return the newly created object, which is also the result of
	 * the call to {@link Joinpoint#proceed()}; might be replaced by
	 * the interceptor
	 * @throws Throwable if the interceptors or the target object
	 * throws an exception
	 */
	/**
	 * 实施此方法可以在构造新对象之前和之后执行额外的处理。 
	 * 礼貌的实现当然想调用{@link  Joinpoint＃proceed（）}。 
	 *  @param调用构造连接点
	 * @return 新创建的对象，这也是对{@link  Joinpoint＃proceed（）}的调用的结果。 
	 * 如果拦截器或目标对象引发异常，则可将其替换为拦截器
	 * @throws 可抛出
	 */
	Object construct(ConstructorInvocation invocation) throws Throwable;

}

```

## 运行环境

- Python 3.6+

- googletrans 2.4.0+

```bash
pip install googletrans -i https://pypi.doubanio.com/simple/
```

## 机翻不准确

如果遇到效果图这样的机翻不准确，甚至让人啼笑皆非，请尝试以下命令将googletrans更新到最新版本，googletrans作者一般会及时更新

``````bash
pip uninstall googletrans
git clone git@github.com:ssut/py-googletrans.git
cd ./py-googletrans && python setup.py install 
``````

## 使用方法

```bash
python3 main.py project_root_dir # e.g python main.py C:\Users\Murphy|IdeaProjects\
```

## 使用案例
[spring-framework机翻](https://github.com/murphy-li/spring-framework)，这个源代码机翻会逐渐更新、完善。


## 待完善
- 其他注释支持
- ~~想用正则匹配注释，但是匹配了怎么替换文本？（已使用正则表达式）~~
- ~~python多线程令人头痛~~
- 每个注释发起一个翻译请求，一个请求握手挥手就很多次，非常浪费资源
- 注释中包含代码块，但是也被机翻了。```<pre class="code">code area</pre>```（参考示例机翻中的代码效果：<pre class = code>类DebuggingInterceptor实现了......）

## 贡献者
[Contributors](https://github.com/murphy-li/english-annotation-buster/graphs/contributors)

## License

[![license](https://img.shields.io/badge/license-Apache%20License%202.0-brightgreen.svg?style=flat)](https://github.com/murphy-li/Clipboard2Voice/blob/master/LICENSE). [点击这里](LICENSE) 获取更多细节。
