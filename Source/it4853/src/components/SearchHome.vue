<template>
    <div class="container">
        <div>
            <label></label>
            <input v-model="query" class="search_input" type="text" placeholder="Type anything ..." />
            <button @click="submit(0)">Search</button>
        </div>
        <div class="container-result" v-if="data != null">
            <p class="result">Kết quả tìm kiếm</p>
            <div class="container-items">
                <div class="items" v-for="item in data" :key="item.id">
                    <a
                        :href="'https://shopee.vn/'+getLink(item.name[0])+'.'+item.shopid+'.'+item.id"
                        target="_blank"
                    >
                        <img width="100%" :src="'https://cf.shopee.vn/file/'+item.image[0]" />
                        <div class="name-item">{{item.name[0]}}</div>
                        <div class="address-item">Địa chỉ: {{item.location[0]}}</div>
                        <div class="price-item">Giá: {{item.price[0].replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')}}</div>
                        <div class="rate-item">Đánh giá: {{item.rating_star[0]}}</div>
                    </a>
                </div>
            </div>
        </div>
        <div class="pagination">
            <span>
                <span :class="{hidden : (pageCurrent==0)}" @click="submit(pageCurrent-1)">&laquo;</span>
            </span>
            <span v-for="page in pages" :key="page">
                <span
                    v-if="page >= pageCurrent && page < pageCurrent+6"
                    @click="submit(page)"
                    :class="{active : (pageCurrent==page)}"
                >{{page+1}}</span>
            </span>
            <span>
                <span @click="submit(pageCurrent+1)">&raquo;</span>
            </span>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "SearchHome",
    data() {
        return {
            data: null,
            query: "",
            numFound: 0,
            numPage: 0,
            pageCurrent: 0,
            pages: []
        };
    },
    methods: {
        async submit(page) {
            let headers = {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            };
            let res = await axios.get(
                "http://localhost:8983/solr/phone-data/select?indent=on&q=*" +
                    `${this.query}` +
                    "*&wt=json" +
                    "&start=" +
                    page * 10,
                headers
            );
            if (res.status !== 200) {
                alert("Đã xảy ra lỗi !!!");
            }

            this.data = res.data.response.docs;
            this.numFound = res.data.response.numFound;
            this.numPage = this.numFound / 10;
            this.pageCurrent = page;
            this.pages = [];
            for (let i = 0; i < this.numPage; i++) this.pages.push(i);
            console.log(res);
        },
        getLink(name) {
            let regex = "+-/%@";
            let link = name.split(" ");
            for (let s in link) {
                if (regex.includes(link[s])) link[s] = "-";
            }
            link = link.join(" ");
            link = link.replace(/ /g, "-");
            return link + "-i";
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
    font-weight: normal;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
    text-decoration: none;
}
.search_input {
    width: 50%;
    border: solid 2px #4272b9;
    border-radius: 10px;
    padding: 20px;
}
input:focus {
    outline: none;
    border: solid 2px #063377;
}
.container-result {
    justify-content: center;
}
.result {
    height: 28px;
    font-family: SFD-Medium;
    font-size: 20px;
    line-height: 28px;
    color: #f77638;
}
.container-items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.items {
    border: 1px solid transparent;
    border-radius: 10px;
    padding-right: 0.3125rem;
    padding-left: 0.3125rem;
    max-width: 200px;
    margin: 10px;
    background: #fff;
}
.items:hover {
    border: 1px solid #ee4d2d;
    border-radius: 10px;
}
.name-item {
    padding: 10px 0px;
    font-weight: bold;
}
.address-item {
    padding: 10px 0px;
}
.pagination {
    margin-top: 50px;
    display: inline-block;
}

.pagination span span {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    transition: background-color 0.3s;
    border: 1px solid #ddd;
    margin: 0 4px;
    cursor: pointer;
}

.pagination span span.active {
    background-color: #4caf50;
    color: white;
    border: 1px solid #4caf50;
}
.hidden {
    visibility: hidden;
}
</style>
