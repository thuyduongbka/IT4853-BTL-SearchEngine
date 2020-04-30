<template>
    <div class="container">
        <form>
            <div>
                <h1>Tìm kiếm điện thoại - So sánh giá</h1>
            </div>
            <form @submit="submit">
                <label></label>
                <input v-model="test"  class="search_input" type="text" placeholder="Type anything ..." />
            </form>
            <p>Thông điệp: {{ test }}</p>
        </form>
        <div class="container-items" v-if="data != null">
            <div class="items">
                <div class="name-item">{{data}}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "SearchHome",
    data () {
        return {
            data:null,
            test:""
        };
    },
    methods: {
        async submit(event) {
            let headers = {
              'Access-Control-Allow-Origin': '*',
              "Content-Type": "application/json"

            }
            console.log(this.test)
             event.preventDefault()
         let res= await axios.get("http://localhost:8983/solr/test/select?indent=on&q=*"+`${this.test}`+"*&wt=json",headers)
         if(res.status!==200){
             alert("Đã xảy ra lỗi !!!")
         }
         this.data=res
         console.log(this.data.data.response.docs)
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
}
.search_input {
    width: 50%;
    border: solid 2px #42b983;
    border-radius: 20px;
    padding: 20px;
}
input:focus {
    outline: none;
    border: solid 2px #034427;
}
.container-items {
    display: flex;
    flex-wrap: wrap;
}
.items {
    max-width: 100px;
}
</style>
