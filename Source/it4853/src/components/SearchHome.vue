<template>
    <div class="container">
        <form>
            <form @submit="submit">
                <label></label>
                <input v-model="test"  class="search_input" type="text" placeholder="Type anything ..." />
            </form>
        </form>
            <div class="container-result"  v-if="data != null">      
                <p class="result">seach results</p> 
                <div class="container-items">
                    <div class="items" v-for="item in data" :key="item">
                        <div class="name-item">{{item.name[0]}}</div>
                        <div class="address-item">Địa chỉ: {{item.location[0]}}</div>
                        <div class="rate-item">Đánh giá: {{item.rating_star[0]}}</div>
                    </div>
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
         let res= await axios.get("http://localhost:8983/solr/BTL/select?indent=on&q=*"+`${this.test}`+"*&wt=json",headers)
         if(res.status!==200){
             alert("Đã xảy ra lỗi !!!")
         }
         this.data=res.data.response.docs
         console.log(this.data)
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
    border: solid 2px #4272b9;
    border-radius: 10px;
    padding: 20px;
}
input:focus {
    outline: none;
    border: solid 2px #063377;
}
.container-result{
    justify-content: center;
}
.result{
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
    padding-right: .3125rem;
    padding-left: .3125rem;
    max-width: 200px;
    margin: 10px;   
    background: #fff;
}
.items:hover{
    border: 1px solid #ee4d2d;
    border-radius: 10px;
}
.name-item{
    padding: 10px 0px;
    font-weight: bold;
}
.address-item{
    padding: 10px 0px;
}
</style>
