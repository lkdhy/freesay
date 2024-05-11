import instance from "@/request/http";

interface ReqShare {
    username: string
    description: string
}
//一般情况下，接口类型会放到一个文件
// 下面两个TS接口，表示要传的参数
interface ReqLogin {
    username: string
    password: string
}

interface ReqRegister {
    username: string
    password: string
    first_name: string
    last_name: string
    email: string
}

interface ReqStatus {
    id: string
    navStatus: string
}

interface User {
    is_active: boolean,
    username: string,
    email: string,
    is_superuser: boolean,
    first_name: string,
    last_name: string
    signature: string,
    isAdmin: boolean
}

interface Box {
    username: string,
    description: string
}
interface Post {
    username: string,
    hostUsername: string,
    question: string
}
// interface GetPost {
//     username: string,
//     public: boolean,
//     answered: boolean
//     answer: string
// }
interface GotPost {
    id: number
    username: string
    question: string
    answer: string
    is_public: boolean
}

// Res是返回的参数，T是泛型，需要自己定义，返回对数统一管理***
type Res<T> = Promise<ItypeAPI<T>>;
type BoxRes<T> = Promise<BoxItypeAPI<T>>;
type GotPostRes<T> = Promise<GotPostItypeAPI<T>>
// 一般情况下响应数据返回的这三个参数，
// 但不排除后端返回其它的可能性，
interface GotPostItypeAPI<T> {
    success: string | null // 返回状态码的信息，如请求成功等;
    result: T,//请求的数据，用泛型
    msg: string | null // 返回状态码的信息，如请求成功等
    message: string
    code: number //返回后端自c定义的200，404，500这种状态码
    post: GotPost
    posts: GotPost[]
    total_posts: number
    // total_pages: number
}
interface BoxItypeAPI<T> {
    success: string | null // 返回状态码的信息，如请求成功等;
    result: T,//请求的数据，用泛型
    msg: string | null // 返回状态码的信息，如请求成功等
    message: string
    code: number //返回后端自c定义的200，404，500这种状态码
    box: Box
    boxes: Box[]
    total_boxes: number
    // total_pages: number
}
interface ItypeAPI<T> {
    success: string | null // 返回状态码的信息，如请求成功等;
    result: T,//请求的数据，用泛型
    msg: string | null // 返回状态码的信息，如请求成功等
    message:string
    code: number //返回后端自定义的200，404，500这种状态码
    user: User
    users: User[]
    total_users: number
    total_pages: number
    isAdmin: boolean
}
interface ItypeAPI_2<T> {
    success: string | null
    msg: string | null
    code: number
//     TODO
}

// my APIs
export const GetBoxApi = (): BoxRes<null> =>
    instance.get('/api/box');
export const ShareApi = (data: ReqShare): Res<null> =>
    instance.post('/api/share', data);
export const PostApi = (data: Post): Res<null> =>
    instance.post(`/api/post`, data);
export const GetPostApi = (params: { 'username': string } ): GotPostRes<null> =>
    instance.get('/api/getpost', {params})
export const AnswerApi = (params: { 'id': number, 'answer': string, 'is_public': boolean } ): Res<null> =>
    instance.post('/api/answer', params)

export const GetHostPostApi = (params: { 'username': string } ): GotPostRes<null> =>
    instance.get('/api/gethostpost', {params})

//测试hello api
export const TestHello = (): Res<null> =>
    instance.get('/api/hello');

//登录 api
export const LoginApi = (data: ReqLogin): Res<null> =>
    instance.post('/api/login', data);

//注册 api
export const RegisterApi = (data: ReqRegister): Res<null> =>
    instance.post('/api/register', data);

//登出 api
export const LogoutApi = (): Res<null> =>
    instance.get('/api/logout');

//根据username查询用户信息api  get
export const GetUserInfoByUserName = (params: { userName: string }): Res<null> =>
    instance.get(`/api/find/${params.userName}`, {params});

//根据pageNumber查询用户信息api  get
export const GetUserInfoByPageNum = (params: { pageNumber: number }): Res<null> =>
    instance.get(`/api/users/list/${params.pageNumber}`, {params});

//以下是模板:
// post请求 ，没参数
export const LogoutAPI = (): Res<null> =>
    instance.post("/admin/logout");

// post请求，有参数,如传用户名和密码
export const loginAPI = (data: ReqLogin): Res<string> =>
    instance.post("/admin/login", data);

// post请求 ，没参数，但要路径传参
export const StatusAPI = (data: ReqStatus): Res<null> =>
    instance.post(`/productCategory?ids=${data.id}&navStatus=${data.navStatus}`);
//  get请求，没参数， export const FlashSessionListApi = (): Res<null> => instance.get("/flashSession/list"); // get请求，有参数，路径也要传参  (也可能直接在这写类型，不过不建议,大点的项目会维护一麻烦) export const ProductCategoryApi = (params: { parentId: number }): any => instance.get(`/productCategory/list/${params.parentId}`, {params}); // get请求，有参数，(如果你不会写类型也可以使用any,不过不建议,因为用了之后 和没写TS一样)
export const AdminListAPI = (params: any): any =>
    instance.get("/admin/list", {params});
