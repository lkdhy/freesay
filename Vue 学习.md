## Vue 学习 _ *20240506*

First Authors: chatGPT-3.5, chatGPT-4；编辑：lch。

* 官方文档：[Introduction | Vue.js (vuejs.org)](https://vuejs.org/guide/introduction.html)

* element-plus官网：[一个 Vue 3 UI 框架 | Element Plus (element-plus.org)](https://element-plus.org/zh-CN/)

  > 数据库(H)助教演示使用了 element-plus
  >
  > > ==element-plus组件的文档写得都挺好的，还可以直接阅读给出的组件示例的源代码了解学习 Vue==

> Vue和React是目前非常流行的两个前端框架，二者都有各自的优点和特性。
>
> 1. 学习曲线：Vue的学习曲线相对较平稳，它的设计思想和编程范式都更接近传统的前端开发，对于初学者来说更友好。而React的学习曲线较陡峭，它采用了一些函数式编程的思想，需要一定的编程基础才能快速上手。
> 2. 性能：Vue和React的性能差异并不大，都非常快。React在虚拟DOM的实现上稍微复杂一些，但并不影响其运行效率。
> 3. 社区和生态：React的社区更大，生态更丰富。React由Facebook维护，有大量的开源库和工具可以使用。Vue的社区相对较小，但仍然有很多优秀的开源库。
> 4. 状态管理：React通过Redux和MobX等库进行状态管理，而Vue则内置了Vuex进行状态管理。
> 5. 模版和组件化：Vue使用了模板系统，更易于编写和理解。而React则全部采用JavaScript，通过JSX进行组件化开发，这也是React的一大特色。
>
> 两者选择哪个，主要取决于你的项目需求和个人喜好。如果你是初学者，或者希望能快速开发一个项目，Vue可能是更好的选择。如果你希望有更丰富的生态和更强大的性能，或者你已经有了一定的编程基础，React可能是更好的选择

[TOC]

### `.vue` 文件

#### 结构

==一个 .vue 文件在 Vue3 中通常包含三个部分：模板（template）、脚本（script）、样式（style）==。它们分别对应着一个组件的结构、行为、样式。

1. **模板（template）：**这部分负责描述组件的HTML结构。它使用了<u>扩展的HTML语法，可以直接包含数据绑定、条件显示、列表渲染等操作</u>。
2. **脚本（script）：**这部分负责处理组件的行为，定义数据、方法等。它使用了Javascript或其衍生语言如TypeScript。
3. **样式（style）：**这部分负责处理组件的样式，使用了CSS或其衍生语言如SCSS、LESS等。

以下是一个基本的 .vue 文件结构：

```vue
<template>
  <div>
    <!-- HTML goes here -->
  </div>
</template>

<script>
export default {
  // JavaScript goes here
}
</script>

<style scoped>
/* CSS goes here */
</style>
```

.vue 文件是 Vue.js 的单文件组件（Single File Components）的概念的实现。**它将一个组件的结构、行为、样式整合到了一个文件中，使得组件的开发更为集中和方便。它也使得组件的复用、测试和维护更为容易。这就是 .vue 文件的意义。**

> 在 Vue3 中，`<style scoped>` 是一种 CSS 作用域的方式，它可以使得当前组件的样式不会影响到其他的组件。这是因为在编译的过程中，Vue会为每个组件的元素添加一个独一无二的属性，例如`data-v-21e5b78`，然后在 CSS 选择器中也添加这个属性，使得 CSS 只能匹配到带有这个属性的元素。
>
> 例如，我们有如下的 Vue 组件：
>
> ```vue
> <template>
>   <div class="example">Hello Vue3!</div>
> </template>
> 
> <style scoped>
> .example {
>   color: red;
> }
> </style>
> ```
>
> 在编译后，HTML 会变成：
>
> ```html
> <div class="example" data-v-21e5b78>Hello Vue3!</div>
> ```
>
> CSS 会变成：
>
> ```css
> .example[data-v-21e5b78] {
>   color: red;
> }
> ```
>
> 这样，`.example` 这个样式就只会作用在带有 `data-v-21e5b78` 属性的元素上，也就是它只会影响到当前的 Vue 组件，而不会影响到其他的组件。
>
> 所以，`<style scoped>` 是一种很好的方式，可以帮助我们更好地管理和维护我们的样式，避免样式的冲突和覆盖。

#### `template`

Vue 中的 template 标签是一种定义模板的方式，它用于声明 Vue 组件的 HTML 结构。这种标签不会被渲染到最终的 HTML 中，而是作为 Vue 实例或组件的模板存在，并被 Vue 的编译器编译为虚拟 DOM。

在 template 标签内部，你可以写入任何有效的 HTML 代码，也可以使用 Vue 提供的一些特殊的模板语法，如 v-if，v-for，v-model等。

使用 template 标签可以使代码更加结构化和易于维护，同时还可以提高应用的性能，因为 Vue 在编译过程中会对 template 进行优化。

例如：

```vue
<template>
  <div>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "Hello, Vue!",
      message: "This is a message."
    };
  }
};
</script>
```

在这个例子中，template 标签内的内容定义了一个 Vue 组件的模板，`{{ title }}` 和 `{{ message }}` 是 Vue 的插值表达式，会被替换为对应的数据。

#### 有关比较

在 Vue 2 中，我们可以通过 `Vue.extend` 来创建一个组件。而在 Vue 3 中，`.vue` 文件的功能相当于 Vue 2 中使用 `Vue.extend` 的组件创建方式。`.vue` 文件提供了一种更方便和直观的方式来组织和编写组件代码，它将模板、样式和逻辑代码都放在同一个文件中，使得组件的开发和维护更加简单和清晰。

在 Vue 3 中，你可以直接使用这种 `.vue` 文件的方式来定义和使用组件，而不需要显式地调用 `Vue.extend` 方法。当我们在其他组件中引用这个 `.vue` 文件时，就相当于在 Vue2 中使用 `Vue.extend()` 创建的构造器创建了一个新的 Vue 实例。

### SFC 基本

```vue
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped>
button {
  font-weight: bold;
}
</style>
```

SFC is a defining feature of Vue and is the recommended way to author Vue components **if** your use case warrants a build setup. You can learn more about the [how and why of SFC](https://vuejs.org/guide/scaling-up/sfc.html) in its dedicated section - but for now, just know that Vue will handle all the build tools setup for you.

> 浏览器本身无法直接渲染 Vue 的单文件组件（Single-File Components，SFC）。Vue 的 SFC 需要通过特定的加载器（如 vue-loader 或 vueify）处理后才能在浏览器中运行。这些加载器会将 SFC 文件中的模板、脚本和样式等内容分别处理，并最终编译成浏览器可以解析的 JavaScript。

### API

> 在 Vue 中有两种不同的 API 模式：Options API 和 Composition API。
>
> 1. Options API 是 Vue 2.x 中广为人知的 API 模式，它基于组件选项对象，将组件的逻辑和模板相关的选项分别放在不同的属性中，比如 data、methods、computed、watch 等，使得组件的结构清晰，易于理解。Options API 是一种传统的方式，适合小型项目或者初学者使用。
> 2. Composition API 是 Vue 3.x 中引入的新的 API 模式，它基于函数式的组合方式，允许将相关代码组织在一起，提高了代码的可复用性和可维护性。Composition API 将组件的逻辑按照功能划分为多个函数，可以更灵活地组织代码，减少逻辑重复。Composition API 更适合大型项目或者需要更好代码组织的情况下使用。
>
> 理解这两种 API 模式可以根据项目需求和个人喜好选择合适的方式来开发 Vue 应用。

#### 选项模式

```vue
<script>
export default {
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
    return {
      count: 0
    }
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    increment() {
      this.count++
    }
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

#### 组合模式

```vue
<script setup>
import { ref, onMounted } from 'vue'

// reactive state
const count = ref(0)

// functions that mutate state and trigger updates
function increment() {
  count.value++
}

// lifecycle hooks
onMounted(() => {
  console.log(`The initial count is ${count.value}.`)
})
    
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>
```

### 常见构建方式

> Vue项目的常见构建方式主要有以下几种：
>
> 1. 使用Vue-cli脚手架工具：Vue-cli是Vue官方提供的一种脚手架工具，可以帮助我们快速创建一个Vue项目，它内部已经配置好了webpack、babel等工具，我们只需按照步骤创建一个新项目，然后就可以开始我们的开发工作了。
> 2. 手动配置Webpack：如果你想对项目的构建过程有更多的控制，你可以选择手动配置Webpack。这种方式需要你对Webpack有一定的了解，你需要自己配置各种loader和plugin，以满足你的项目需求。
> 3. 使用CDN：这是一种最简单的方式，你只需要在你的HTML文件中引入Vue.js的CDN链接，然后就可以开始写Vue代码了。这种方式适合一些小的、不需要构建过程的项目。
> 4. 使用Nuxt.js：对于需要服务端渲染（SSR）的Vue项目，可以选择使用Nuxt.js。Nuxt.js是一个基于Vue.js的通用应用框架，内部集成了Vue、Vue Router、Vuex等库，以及webpack、Babel等工具，可以帮助我们快速构建服务端渲染的Vue项目。
> 5. 使用VuePress：对于需要构建静态网站的Vue项目，可以选择使用VuePress。VuePress是一个基于Vue的静态网站生成器，适合用来构建技术文档、博客等静态网站。

* `npm init vue@latest` 是npm 6.1版以后的新命令，可以用来快速初始化一个Vue项目。它更像是一个快捷方式，会自动创建项目文件夹，同时安装必要的依赖包，包括Vue框架。当然，这需要你已经全局安装了create-vue模块。
* 而`npm install vue`则是直接安装Vue框架本身，不会创建项目文件夹，也不会安装其他依赖包，只是单纯的将Vue框架安装到当前目录下的node_modules文件夹。

总的来说，`npm init vue@latest`是一个完整的项目初始化命令，而`npm install vue`则是一个单纯的框架安装命令。

[npm create vite@latest 和 npm init vue@latest 的区别](https://www.cnblogs.com/workbox/p/17829466.html)？？？（真的有区别吗？——lch）

---

==`npm run dev`== 命令的作用就是运行在 package.json 文件中定义的 "dev" 脚本，通常用于启动开发环境。在大部分的前端项目中，"npm run dev" 命令会启动一个本地的开发服务器，并且在你保存文件的时候自动刷新页面。

#### Vite

> Vite 和 Vue-cli 都是 Vue.js 的构建工具，可以帮助开发者快速搭建和配置 Vue 项目。不过，二者在设计理念和技术实现上有所不同。
>
> Vue-cli 是早期 Vue.js 的官方脚手架工具，它提供了一套完整的项目构建解决方案，包括项目初始化、开发、打包等功能。Vue-cli 使用的是 Webpack 作为打包工具，Webpack 会将所有的模块打包成一个 JavaScript 文件，然后在浏览器中运行。这种方式在开发阶段可能会导致启动和更新速度较慢，特别是在大型项目中。
>
> Vite 是由 Vue.js 的作者尤雨溪开发的一款新型前端构建工具，它的目标是提供一个更快、更轻量的开发环境。Vite 在开发模式下不需要打包，可以直接将源码转换成浏览器可以识别的 ES Modules，极大地提升了初始启动和热更新的速度。Vite 还内置了对 Vue 3 的支持，以及对 TypeScript、CSS Pre-processors 等现代前端技术的支持。
>
> 总的来说，Vite 和 Vue-cli 的主要区别在于打包策略和开发体验。Vite 提供了更快的启动和热更新，以及对 Vue 3 的原生支持，适合用于构建现代化的 Vue 项目。而 Vue-cli 则提供了一套成熟的项目构建解决方案，适合用于构建复杂的、需要大量定制的 Vue 项目。根据项目的需求和团队的技术栈来选择最适合的工具。

### 路由

> 在前端开发中，路由是一种映射关系，它负责将特定的URL映射到特定的页面或者组件。这样做是为了方便用户在不同的页面间跳转。
>
> 举个例子，如果你有一个博客网站，可能会有一个URL是"www.yourblog.com/posts"，这个URL就对应了所有博客文章的列表页面，而"www.yourblog.com/posts/1"可能就对应了第一篇博客文章的内容页面。这些URL和页面之间的对应关系，就是通过路由来实现的。
>
> 在传统的网站开发中，这种路由通常是由服务器来处理的。比如使用PHP或者Java开发的网站，当用户访问一个URL时，服务器会根据路由找到对应的页面文件，然后将其发送给浏览器。
>
> 但是在现代的前端开发中，尤其是使用React、Vue等前端框架开发单页面应用（SPA）时，路由就变成了前端的工作。因为在SPA中，页面不再是服务器渲染出来的，而是由前端的JavaScript代码生成的。所以，前端需要根据URL来决定显示哪个页面或者组件，这就需要使用到前端路由。
>
> 总的来说，前端路由就是一种机制，它能够让前端应用根据URL的变化，显示不同的内容，提供不同的用户交互。

Vue中的路由是一个非常重要的概念，它主要用于构建单页面应用。在单页面应用中，页面不需要刷新就可以加载不同的内容，这就需要路由来控制。

Vue路由，全称为Vue Router，是一个专门为Vue.js设计的路由系统，它可以通过改变浏览器的URL，驱动Vue实例展示不同的内容，实现页面跳转，而不需要重新加载。

基本上，路由就是根据网址的不同，返回不同的内容或页面。以一个博客网站为例，当你点击一个博客标题时，浏览器的URL可能会变成 [www.blogsite.com/posts/1。这个/posts/1就是路由，它告诉浏览器，用户想要查看ID为1的博客内容。](http://www.blogsite.com/posts/1。这个/posts/1就是路由，它告诉浏览器，用户想要查看ID为1的博客内容。)

在Vue中，定义路由非常简单，只需要创建一个Vue Router实例，然后定义路由规则，最后将其挂载到Vue实例上。其中，路由规则是一个数组，每个元素是一个路由对象，对象中的path属性定义了路由的路径，component属性则指向了对应的Vue组件，当URL匹配到某个路由规则时，就会展示对应的组件。

总的来说，Vue中的路由是帮助我们构建单页面应用的关键工具，它通过改变URL和控制组件的显示，让我们能够在不刷新页面的情况下，展示不同的内容。

### Vue 特性与用法

#### `import` 导入

import 是 ES6 中用于导入模块的关键字。在使用 Vue.js 进行开发时，我们通常会用到 import，比如导入组件、函数库等。

import 的基本语法如下：

```typescript
import defaultExport from "module-name";
import * as name from "module-name";
import { export } from "module-name";
import { export as alias } from "module-name";
import { export1 , export2 } from "module-name";
import { export1 , export2 as alias2 , [...] } from "module-name";
import defaultExport, { export [ , [...] ] } from "module-name";
import defaultExport, * as name from "module-name";
import "module-name";
```

1. 第一种情况：默认导出。每个模块都可以有一个默认导出，对应的 import 语句中不需要使用大括号。
2. 第二种情况：导入整个模块。这样可以将整个模块作为一个变量，然后通过这个变量来访问模块的各个属性。
3. 第三种情况：导入模块的部分内容。大括号中的变量名必须与导出时的名字一致。
4. 第四种情况：为导入的变量取别名。可以使用 as 关键字为导入的变量取别名。
5. 第五种情况：一次导入模块的多个内容。
6. 第六种情况：对导入的内容进行选择和重命名。
7. 第七种情况：同时导入默认内容和其他内容。
8. 第八种情况：将默认导出内容和所有其他导出内容一起导入。
9. 第九种情况：只加载模块，但是不导入任何内容。

在 TypeScript 中，import 的使用基本同 JavaScript，但是 TypeScript 还支持类型导入和类型导出，以支持静态类型检查和工具支持。

总的来说，import 的用法是多样的，可以根据需要导入全模块，也可以只导入部分内容，或者将导入的内容重命名等等。这大大增加了代码的灵活性，并有助于模块化的编程。

#### `ref` 和 `reactive` API

`ref` 是 Vue 3 中一个十分重要的响应式引用API。它用于创建一个响应式的数据对象，我们可以把它想象成一个可以存储数据并且这个数据是响应式的盒子。当我们改变这个盒子里面的数据时，Vue 3 会自动检测到这个变化并更新视图。

`ref` 在 Vue 3 中的使用方法非常简单。首先，我们需要从 `vue` 包中导入 `ref` 函数，然后使用它来创建一个响应式的数据对象。

例如：

```typescript
import { ref } from 'vue';

export default {
  setup() {
    const count = ref(0);

    const increment = () => {
      count.value++;
    };

    return {
      count,
      increment
    };
  }
};
```

在上述代码中，我们首先导入了 `ref` 函数，然后在 `setup` 方法中使用它来创建了一个初始值为 0 的响应式数据 `count`。然后，我们定义了一个 `increment` 方法，用于增加 `count` 的值。注意我们通过 `count.value` 来获取和修改 `count` 的值。

最后，我们需要返回 `count` 和 `increment`，以便在模板中使用它们。

在模板中，我们可以直接使用 `count` 和 `increment`：

```vue
<template>
  <div>{{ count }}</div>
  <button @click="increment">Increment</button>
</template>
```

当点击按钮时，`count` 的值会增加，同时视图也会自动更新。

Vue3 中的 `reactive` 和 `ref` 都是用来创建响应式数据的 API。它们的主要区别在于，`reactive` 是将一个对象转换为响应式对象，而 `ref` 则是将一个基本类型的值转换为响应式对象。

---

`reactive` 可以接受一个普通对象然后返回该普通对象的响应式副本。响应式转换是“深层”的——也就是说它影响对象内部的所有嵌套属性。基于 ES2015 的 Proxy 实现，`reactive` 返回的对象不等同于原始对象。建议仅使用响应式代理，而避免依赖原始对象。

```
import { reactive } from 'vue'

const obj = reactive({ count: 0 })
```

#### 插件 `.use`

在Vue3中，`.use`是一个全局API，主要用于注册插件。这个API接收一个插件作为其参数，并且调用这个插件的`install`方法，将Vue实例作为其参数。

在Vue的插件系统中，一个插件应该暴露一个`install`方法。这个方法将会在`.use`被调用时执行。这个`install`方法的第一个参数是Vue构造器，第二个参数是一个可选的选项对象。

例如，如果你有一个插件如下：

```typescript
const MyPlugin = {
  install(Vue, options) {
    // 插件代码
  }
}
```

你可以在Vue中使用这个插件：

```typescript
const app = createApp(App)
app.use(MyPlugin)
app.mount('#app')
```

`.use`的主要目的是使得插件代码可以在Vue实例创建之前运行，这样插件就可以有机会修改Vue实例或向其添加新的功能。

#### `slot`

> 如何理解Vue里面的 <slot name="icon"></slot>，slot是html标签吗

在 Vue 中，`<slot></slot>` 不是 HTML 标签，而是 Vue 组件的一部分，用于实现内容分发。具体来说，它允许你在使用自定义组件时在组件中嵌入额外的内容。

例如，你有一个自定义的按钮组件，你想在这个按钮的文字旁边添加一个图标。你可以使用 `<slot>` 标签在你的组件模板中预留一个位置，然后在使用这个组件的地方插入你的图标。

`<slot name="icon"></slot>` 是一个命名插槽，你可以在使用组件的地方通过 `slot` 属性为这个插槽插入特定的内容。例如：

```vue
<my-button>
  <img slot="icon" src="my-icon.png" />
  Click me
</my-button>
```

在这个例子中，`<img slot="icon" src="my-icon.png" />` 将会被插入到 `my-button` 组件中 `name` 为 `"icon"` 的插槽的位置。而 `Click me` 文字则会被插入到默认的插槽（没有 `name` 属性的插槽）中。

----

> 在大语言模型的prompt中，如果没有“system”，模型仍然能够生成回复，但可能没有特定的指导或者上下文信息。"System"通常用于设置对话的上下文，指示模型提供特定类型的回答或引导模型的对话方向。如果没有"system"，模型将根据给定的其他输入进行回答。
>
> 例如，如果你输入 "Translate 'Hello' to French"，即使没有“system”，模型仍然能够理解你的请求并给出正确的法语翻译。然而，如果你想要模型以特定的方式回答或遵循特定的对话格式，使用"system"可以帮助提供这样的指导。
>
> 需要注意的是，不同的语言模型可能会对"system"的缺失有不同的反应，这取决于它们的训练方式和使用的数据。

### Vue 生态系统

Vue 生态是指与 Vue.js 框架相关的生态系统，包括各种工具、插件和库，为开发者提供丰富的资源和支持。Vue 生态系统包括但不限于以下内容：

1. Vue Router：用于构建单页面应用程序的官方路由管理器。
2. Vuex：用于管理 Vue.js 应用程序中的状态的官方状态管理库。
3. Vue CLI：官方的脚手架工具，用于快速搭建 Vue.js 项目。
4. Vue Devtools：在浏览器中调试 Vue.js 应用程序的开发者工具。
5. Element UI、Vuetify、Ant Design Vue 等 UI 组件库，提供了丰富的 UI 组件来加速开发。
6. Nuxt.js：基于 Vue.js 的通用应用框架，用于快速开发服务器渲染应用程序。
7. Vue Test Utils：官方的测试工具库，用于编写单元测试和集成测试。

这些工具和库构成了 Vue 生态系统，为 Vue.js 开发者提供了完整的解决方案，帮助他们更高效地构建现代 Web 应用程序。

#### axios

[Getting Started | Axios Docs (axios-http.com)](https://axios-http.com/docs/intro)

**Axios** 是一个基于 Promise 的 HTTP 库，可以用在浏览器和 node.js 中。在 Vue.js 中，我们可以使用 axios 来发送 HTTP 请求，包括 GET，POST，PUT，DELETE等等。Axios 的特性主要包括：

1. 在浏览器中发送 XMLHttpRequests
2. 在 node.js 中发送 http 请求
3. 支持 Promise API
4. 能够拦截请求和响应
5. 能够转换请求和响应数据
6. 能够取消请求
7. 自动转换 JSON 数据
8. 在客户端支持防止 CSRF/XSRF

在 Vue 中使用 axios，首先需要在项目中安装 axios：

```
npm install axios --save
```

然后在需要使用的地方引入 axios：

```typescript
import axios from 'axios';

// 发送 GET 请求
axios.get('/user?ID=12345')
  .then(function (response) {
    // 处理响应数据
  })
  .catch(function (error) {
    // 处理错误
  });

// 发送 POST 请求
axios.post('/user', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  .then(function (response) {
    // 处理响应数据
  })
  .catch(function (error) {
    // 处理错误
  });
```

除此之外，axios 还提供了一些更高级的用法，如并发请求、请求和响应的拦截等。总的来说，axios 是一个功能强大，使用方便的 http 请求库，配合 Vue.js 可以很好地处理前后端的数据交互。

在JS/TS语言中，当函数实参前面加上 `async` 关键字时，表示该函数是一个异步函数。异步函数将返回一个 `Promise` 对象，可以使用 `await` 关键字来等待异步操作的完成。这样可以避免阻塞主线程，提高代码的异步执行效率。异步函数的实现方式是通过将函数的执行过程分为多个阶段，每个阶段都会将结果保存在一个任务队列中，然后在空闲时执行这些任务，从而达到异步执行的效果。



axios 是一个基于 Promise 的 HTTP 请求库，用于发送异步请求。它可以与 Vue.js 框架很好地配合使用。

在 Vue.js 中，通过引入 axios 库，你可以轻松地发送 HTTP 请求，并处理响应数据。axios 提供了一系列的方法，如 `get`、`post`、`put`、`delete` 等，用于发送不同类型的请求。你可以指定请求的 URL、请求参数、请求头等信息，并通过 Promise 的方式处理请求的结果。

以下是一个使用 axios 发送 GET 请求的示例：

```
import axios from 'axios';

axios.get('/api/users')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

在上面的示例中，我们使用 `axios.get` 方法发送一个 GET 请求到 `/api/users` 地址，并在请求成功后通过 `then` 方法处理响应数据，如果请求失败则通过 `catch` 方法处理错误。

除了基本的 GET 请求，axios 还支持发送带有请求体的 POST、PUT、DELETE 等请求，并可以设置请求头、请求超时时间等。

需要注意的是，为了在 Vue.js 中全局使用 axios，你可以将其挂载到 Vue 实例的原型链上，或者使用 Vue 插件的形式进行全局注册。这样在组件中就可以通过 `this.$http` 或 `this.$axios` 访问 axios 实例，方便地发送请求。

总之，axios 是一个功能强大且易于使用的 HTTP 请求库，可以帮助你在 Vue.js 中处理异步请求。



**前端用 axios 发送请求，后端用 django 作为服务器。评述这样设计的可行性和合理性**

这种设计是非常可行和合理的。Axios 是一个流行的前端 HTTP 客户端，它可以轻松地发送异步请求到后端服务器。而 Django 是一个强大的后端框架，可以处理这些请求并提供相应的数据和逻辑处理。

Axios 提供了良好的异步请求处理机制，可以发送 GET、POST 等类型的请求，而 Django 可以很容易地解析这些请求，并根据路由和视图函数来处理它们。这种分离前后端的设计使得代码结构更清晰，前端和后端可以分别进行开发和测试，提高了团队的协作效率。

另外，Axios 和 Django 都有很好的文档和社区支持，开发者可以轻松地获取帮助和资源。因此，使用 Axios 发送请求，后端用 Django 作为服务器的设计，是一种非常可行和合理的选择。

---

### Vue 学习建议

学习Vue时，新手们可能会遇到以下困难和误区：

1. 没有掌握Vue的核心概念：Vue的核心概念包括模板语法、组件、数据绑定、计算属性、生命周期钩子等。如果没有掌握这些概念，就会很难理解Vue的工作原理和使用方法。
2. 对Vue的指令和选项理解不透彻：Vue的指令和选项是Vue提供的一些功能和配置项，包括v-bind、v-on、v-if、computed、watch等。如果对这些指令和选项的使用方法和作用不够清晰，就会导致代码写的不够优雅和易于维护。
3. 缺乏实践经验：学习Vue最重要的是实践，只有通过实践才能更好地理解Vue的使用方法和技巧。如果缺乏实践经验，就会很难掌握Vue的精髓。
4. **==没有学习Vue的周边生态：Vue的周边生态非常丰富，包括Vue Router、Vuex、Axios等。如果没有学习这些工具和插件的使用方法，就会很难应对实际开发中的需求。==**
5. ==没有利用好Vue的官方文档和社区资源：Vue的官方文档和社区资源非常丰富，==包括Vue的官方文档、Vue的GitHub仓库、Vue的论坛和社交媒体等。如果没有利用好这些资源，就会很难快速解决问题和跟上Vue的更新迭代。

---

新手在学习Vue.js时可能会遇到的困难和误区主要包括：

1. 缺乏基础知识：Vue是一个基于JavaScript的前端框架，因此在学习Vue之前，需要对JavaScript有一定的了解。如果对JavaScript的理解不够深入，可能会在应用Vue过程中遇到困难。
2. **==不理解Vue的组件化：Vue使用了一种基于组件的开发模式，这对于新手来说可能是个挑战。新手可能会对如何将页面拆分为一个个组件，如何管理组件间的数据传递等概念感到困惑。==**
3. **==数据绑定理解不深：Vue.js的核心之一是数据驱动，这意味着数据的变化会自动反映到视图上。新手可能会对这个数据和视图的绑定关系理解不深，有时候可能会在数据更新后视图没有按预期更新时感到困惑。==**
4. 对Vue生命周期的理解：每个Vue组件都有其自己的生命周期，新手可能会对这个概念感到困惑，不知道在哪个生命周期阶段去执行特定的操作。
5. 过于依赖插件：由于Vue有丰富的插件库，新手可能会过于依赖插件，而忽视了对Vue本身的理解和学习。
6. 对Vue Router和Vuex的理解：Vue Router和Vuex是Vue的核心插件，分别用于路由管理和状态管理。新手在理解和使用这两个插件时可能会遇到困难。
7. 误区：Vue就是为了解决所有问题。实际上，Vue是一个工具，虽然它强大，但并不是所有情况都适用。在某些情况下，可能原生JavaScript或者其他框架更适合。
8. 误区：忽视性能优化。Vue虽然在设计上尽可能地简化了开发过程，但如果不注意性能优化，仍然可能导致应用性能不佳。

以上就是新手在学习Vue时可能遇到的困难和误区，解决这些问题的关键在于深入理解Vue的设计理念和原理，多实践，逐渐积累经验。

---

### 知识（杂项）学习积累

#### JS / TS 语法

**如何理解 TS 语言中函数前加上 export，以及 export default？JS 语言中有这样的语法吗如何理解 TS 语言中函数前加上 export，以及 export default？JS 语言中有这样的语法吗**

##### `export` 模块导出语法

在 TS（TypeScript）和 JS（JavaScript）中，`export` 和 `export default` 都是模块导出语法的一部分，用于将函数、类、对象或值从模块中导出，以便在其他模块中使用。

`export` 关键字用于导出模块中的命名导出。命名导出可以有多个，但需要使用相应的名字进行导入。例如：

```typescript
// myModule.ts
export function myFunction() {
  // ...
}

// anotherModule.ts
import { myFunction } from './myModule';
myFunction();
```

`export default` 关键字用于导出模块的默认导出。每个模块只能有一个默认导出，导入时可以使用任意名称。例如：

```typescript
// myModule.ts
export default function myFunction() {
  // ...
}

// anotherModule.ts
import anyNameYouWant from './myModule';
anyNameYouWant();
```

JavaScript 也有这样的语法，ES6（ECMAScript 2015）引入了模块系统，它包括 `export` 和 `export default`。TypeScript 作为 JavaScript 的超集，也包含了这些语法。

因此，这些语法旨在帮助我们更好地组织和共享代码，我们可以在一个模块中编写代码，然后导出，以便在其他模块中使用。

##### typescript 的 `interface` 接口语法

**如何理解 typescript 中的 interface 接口**

在 TypeScript 中，interface 接口用于定义对象的结构和属性。它类似于其他编程语言中的接口，用于描述对象应该具有的属性和方法。通过定义接口，可以在代码中明确指定对象的结构，以便在编译时进行类型检查和提供代码提示。

使用 interface 可以帮助开发者在代码中定义特定类型的对象，并且可以在不同的地方重复使用这些定义，从而提高代码的可维护性和可读性。接口可以包含属性、方法、可选属性、只读属性等，从而灵活地定义对象的结构。

总的来说，使用 TypeScript 中的 interface 接口可以帮助开发者更好地定义和管理对象的结构，提高代码的可靠性和可维护性。

##### 如何理解 TS 语言中的“泛型”

"泛型"是一种在定义函数、接口或类时，不预先指定具体的类型，而在使用的时候再指定类型的方式。

在 TS 中，泛型是一种重要的工具，它能创建可重用的组件，一个组件可以支持多种类型的数据，而用户就可以根据自己的需求来使用这些组件。

例如，你需要一个函数来处理数组，但是这个数组可能是任何类型的数组，这个时候你就可以使用泛型：

```typescript
function identity<T>(arg: T[]): T[] {
    return arg;
}
```

在这个函数中，`T` 就是一个类型变量，它代表任何类型。这个函数接受一个任何类型的数组，返回一个同样类型的数组。当我们调用这个函数的时候，可以指定 `T` 的具体类型：

```typescript
let output = identity<string>(["myString"]);
```

通过这种方式，我们可以创建出既保证代码类型安全，又能保持函数或类的可复用性的代码。

> 在 TypeScript（TS）中，泛型（Generics）是一种能够在不同类型之间创建可重用代码的方式。使用泛型可以让我们编写更加灵活和通用的代码，因为它允许我们将类型作为参数传递给函数、类和接口。通过泛型，我们可以编写能够适用于多种类型的代码，而不需要重复编写相似的逻辑。
>
> 在 TS 中，泛型通常使用单个字母（如 T）来表示类型参数，然后在函数、类或接口中使用该类型参数。例如，可以编写一个泛型函数来处理任意类型的数组，而不需要针对每种类型都编写一个函数。
>
> 泛型在 TS 中的使用非常灵活，可以帮助我们提高代码的复用性和可读性。通过理解和灵活运用泛型，我们可以编写更加通用和健壮的代码。

#### html 与 css

##### html 表单

HTML表单是HTML网页中一种收集用户输入的重要工具。它可以包含各种类型的输入元素，如文本字段、复选框、单选按钮和按钮等。

以下是一些HTML表单的常用知识：

1. `<form>`标签：HTML表单使用`<form>`标签来定义。所有的输入元素需要放置在`<form>`标签之间。
2. `<input>`标签：`<input>`标签是最重要的表单元素。`<input>`元素可以是多种类型，例如：文本字段、密码字段、提交按钮、复选框、单选按钮等。通过`type`属性来定义`<input>`元素的类型。
3. `<label>`标签：为`input`元素定义标签，提高用户体验。当用户选择该标签时，就会选中与标签相关的`input`元素。
4. `<textarea>`标签：用于用户输入多行文本。
5. `<select>`和`<option>`标签：用于创建下拉列表。`<option>`标签定义下拉列表中的选项。
6. `<button>`标签：创建一个可点击的按钮。
7. 表单验证：HTML5引入了表单验证的新功能，如必填字段（required）、数字字段（number）、邮箱字段（email）等。
8. `action`属性：定义表单数据提交给服务器端的URL。
9. `method`属性：定义数据提交到服务器的方法，通常是"get"（默认）或"post"。
10. `name`属性：定义唯一的名称，用于服务器端识别各个字段的数据。

这些是HTML表单的一些基础知识，通过组合使用这些元素和属性，可以创建出各种功能的表单，满足各种用户输入需求。

##### 超链接 `<a>`

这个超链接标签中有三个属性：

1. href="https://vuejs.org/": 这个属性定义了链接的目标地址，当用户点击这个链接时，浏览器会跳转到这个地址。在这个例子中，链接将会打开Vue.js的官方网站。
2. target="_blank": 这个属性定义了链接的打开方式。"_blank"的值表示链接将在新的浏览器窗口或者标签页中打开。如果不设置这个属性，链接会在当前窗口或标签页中打开。
3. rel="noopener": 这个属性定义了链接的关系。"noopener"的值表示新打开的页面与原页面之间没有任何关系，新页面无法通过JavaScript的window.opener属性访问原页面。这个属性可以防止新打开的页面通过window.opener属性进行一些恶意的行为，如改变原页面的URL。

---

##### 元素边框 `<border>`

在CSS中，可以使用"border"属性来显示元素的边框。这个属性允许你指定边框的宽度、样式和颜色。

例如，以下的CSS代码会给元素添加一个宽度为1px、样式为实线、颜色为黑色的边框：

```
.element {
  border: 1px solid black;
}
```

在这个例子中，".element"是你想要添加边框的元素的类名。

你也可以分别设置边框的宽度、样式和颜色。例如：

```css
.element {
  border-width: 1px;
  border-style: solid;
  border-color: black;
}
```

此外，你还可以单独设置每一边的边框。例如，以下的代码会给元素的顶部边框设置为红色，其它边框设置为黑色：

```css
.element {
  border: 1px solid black;
  border-top-color: red;
}
```

以上就是在CSS中显示元素边框的方法。

---

##### 长度单位

在CSS中，长度单位有很多种，包括像素（px）、点（pt）、百分比（%）、em等。px和em都是非常常用的长度单位，但他们的定义和使用方式有所不同。

px（像素）是固定的长度单位，它是相对于屏幕的分辨率而言的。比如，如果屏幕分辨率是72DPI（dots per inch，每英寸像素数），那么1px就是屏幕上的一个像素点。因为px是固定的，所以它不会受到父元素字体大小的影响。

em是相对长度单位，它的值并不固定，而是相对于最近的父元素的字体大小。假设父元素的字体大小是16px，那么1em就等于16px。如果父元素的字体大小变化，那么em的值也会相应地变化。

比如，如果我们有如下的CSS样式：

```css
body {
    font-size: 16px;
}
p {
    font-size: 1.5em;
}
```

在这个例子中，段落（p）的字体大小将等于24px（因为1.5em * 16px = 24px）。

因此，px和em的主要区别在于，px是固定的，而em是相对的。使用em可以使我们的网页设计更具有灵活性和可扩展性，特别是在响应式设计中，它可以帮助我们更好地适应不同的屏幕尺寸和分辨率。

##### CSS 的 `flex` 排版

**如何理解 css 中将一个 container的 display 设置成 flex？在这种情况下，其子元素似乎全都挤在中间的同一行，如何换行**

可以使用Flexbox或者CSS Grid来实现这个需求。

1. 使用Flexbox：

```
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
```

`justify-content`和`align-items`属性用于在水平和竖直方向上居中子元素。`flex-direction: column;`则确保每行只有一个元素。

1. 使用CSS Grid：

```
.parent {
  display: grid;
  place-items: center;
  grid-template-columns: repeat(auto-fit, minmax(100%, 1fr));
}
```

`place-items: center;`属性同样用于在水平和竖直方向上居中子元素。`grid-template-columns: repeat(auto-fit, minmax(100%, 1fr));`则确保每行只有一个元素。

#### HTTP 回顾

HTTP（超文本传输协议）是一种用于数据通信的协议，主要用于在万维网上发布和检索HTML网页。HTTP允许浏览器向服务器发送请求，并获取服务器的响应。这是一个无状态的协议，意味着每一次请求都是独立的，服务器不会保存之前的请求信息。

HTTP请求和响应包含了很多信息，包括数据类型、状态码、消息体等。其中，最常见的HTTP方法包括GET（获取资源）、POST（发送数据）、PUT（更新资源）和DELETE（删除资源）。

HTTP协议是基于TCP/IP协议的，因此，HTTP通信需要经过建立连接、数据传输和断开连接三个步骤。而HTTP的主要问题是，数据传输是明文的，容易被监听和篡改，因此，现在大多数网站都使用了HTTPS协议，它是在HTTP上加入了SSL/TLS协议，可以对数据进行加密，保证数据传输的安全。

HTTP协议是Web技术的基础，理解HTTP协议，对于理解Web技术和开发Web应用有很大的帮助。





---

### Python 知识

**python 的 -m 选项加不加有什么区别**

Python 的 -m 选项是用来运行库模块作为脚本。

如果没有加 -m 选项，Python 将会直接运行指定的 python 文件。

如果加了 -m 选项，Python 将会寻找 sys.path 中的 Python 库模块，并运行它。sys.path 是一个 Python 搜索模块的路径列表。这意味着你可以使用 -m 选项来运行安装的模块。

具体举例，如果你想运行一个叫做 script.py 的脚本，你可以直接运行 `python script.py`。但是如果你想运行 Python 的内置 HTTP 服务器，你需要使用 -m 选项，如 `python -m http.server`。你不能直接运行 `python http.server`，因为 http.server 是一个模块，不是一个脚本文件。









![image-20240504224306421](C:\Users\HUAWEI\AppData\Roaming\Typora\typora-user-images\image-20240504224306421.png)