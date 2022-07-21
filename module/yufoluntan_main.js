// JavaScript Documen
const CryptoJS = require('./module/crypto-js.min')
// import CryptoJS from "./crypto-js.min.js";
String.prototype.replaceAll = function (s1, s2) {
	var reg = new RegExp(s1, "g");
	return this.replace(reg, s2);
}
function aes_encrypt(msg,key) {

	var str = CryptoJS.AES.encrypt(msg, key).toString();
	// console.log(str)
	str = str.substring(10);
	return str

}
function encrypt() {
	var msg = $("#text-decryped").val();
	var key = $("#text-key").val();

	if (msg.length < 1) {
		$("#error-alert").show();
		$("#copy-alert").hide();
		$("#error-alert").text("ÎÞÑÔÕß£¬×ÝÕæÉñÔÙÁÙ£¬Òà²»¿É¶É¡££¨ÇëÊäÈë´ý¼ÓÃÜµÄÃ÷ÎÄ£©");
	} else {
		if (key.length < 1) {
			key = password;
		}

		$("#text-encryped").val(togod(msg, key));
		$("#error-alert").hide();
		$("#copy-alert").hide();
	}

}
function  aes_decrypto(msg,key) {
	 return CryptoJS.AES.decrypt("U2FsdGVkX1" + msg, key).toString(CryptoJS.enc.Utf8);
}
function decrypt(msg,key) {

	if (msg.length < 1) {
		return "ÎÞÑÔÕß£¬×ÝÕæÉñÔÙÁÙ£¬Òà²»¿É¶É¡££¨ÇëÊäÈë´ý½âÃÜµÄÃÜÎÄ£©";
	} else {
		if (msg.substring(0, 4) !== "·ðÓÖÔ»£º" || msg.substring(0, 3) !== "·ðÓÖÔ»£º"  ) {
			return "Ê©Ö÷¿ÉÔø¼ÇµÃ´ËÎªºÎ¸ßÉ®ËùÑÔ£¿£¨²»ÊÇ·ðÓï£¬ÇëÈ·¶¨ÃÜÎÄÀ´Ô´±¾ÍøÕ¾²¢ÇÒÃÜÎÄÒÔ¡°·ðÔ»£º¡±»ò¡°·ðÓÖÔ»£º¡±¿ªÍ·¡±£©";
		} else {
			try {
				var str = toman(msg, key);
			} catch (err) {
				return "Ê©Ö÷¿ÉÔø¼ÇµÃ´ËÎªºÎ¸ßÉ®ËùÑÔ£¿£¨·ðÓïÓÐÎó£¬ÇëÈ·¶¨ÃÜÔ¿ÕýÈ·²¢Î´±»´Û¸Ä£©";
			} finally {
			}
			return str
		}
	}
}



function togod(msg, key) {
	var str = CryptoJS.AES.encrypt(msg, key).toString();
	// console.log(str)
	str = str.substring(10);

	str = str.replaceAll("e", "†ª");
	str = str.replaceAll("E", "ôÉ");
	str = str.replaceAll("t", "ÆÅ");
	str = str.replaceAll("T", "Ìá");
	str = str.replaceAll("a", "Ä¦");
	str = str.replaceAll("A", "ˆÊ");
	str = str.replaceAll("o", "Ú­");
	str = str.replaceAll("O", "åÈ");
	str = str.replaceAll("i", "Ò®");
	str = str.replaceAll("I", "¼ª");
	str = str.replaceAll("n", "æ¶");
	str = str.replaceAll("N", "·ð");
	str = str.replaceAll("s", "Ò¹");
	str = str.replaceAll("S", "ÍÔ");
	str = str.replaceAll("h", "ÄÇ");
	str = str.replaceAll("H", "½÷");
	str = str.replaceAll("r", "Ï¤");
	str = str.replaceAll("R", "Ü¯");
	str = str.replaceAll("d", "°¢");
	str = str.replaceAll("D", "ºô");
	str = str.replaceAll("l", "Èø");
	str = str.replaceAll("L", "Äá");
	str = str.replaceAll("c", "ÍÓ");
	str = str.replaceAll("C", "††");
	str = str.replaceAll("u", "†o");
	str = str.replaceAll("U", "ÒÁ");
	str = str.replaceAll("m", "Â¬");
	str = str.replaceAll("M", "ºÈ");
	str = str.replaceAll("w", "µÛ");
	str = str.replaceAll("W", "Ë¸");
	str = str.replaceAll("f", "õµ");
	str = str.replaceAll("F", "ÃÉ");
	str = str.replaceAll("g", "·£");
	str = str.replaceAll("G", "É³");
	str = str.replaceAll("y", "‡´");
	str = str.replaceAll("Y", "Ëû");
	str = str.replaceAll("p", "ÄÏ");
	str = str.replaceAll("P", "¶¹");
	str = str.replaceAll("b", "ÎÞ");
	str = str.replaceAll("B", "ÔÐ");
	str = str.replaceAll("v", "ÆÐ");
	str = str.replaceAll("V", "Ù¤");
	str = str.replaceAll("k", "âò");
	str = str.replaceAll("K", "¾ã");
	str = str.replaceAll("j", "¶ß");
	str = str.replaceAll("J", "¶È");
	str = str.replaceAll("x", "ð«");
	str = str.replaceAll("X", "ê^");
	str = str.replaceAll("q", "ÊÒ");
	str = str.replaceAll("Q", "µØ");
	str = str.replaceAll("z", "Àû");
	str = str.replaceAll("Z", "ÕÚ");
	str = str.replaceAll("0", "ÄÂ");
	str = str.replaceAll("1", "²Î");
	str = str.replaceAll("2", "Éá");
	str = str.replaceAll("3", "ËÕ");
	str = str.replaceAll("4", "²§");
	str = str.replaceAll("5", "Ò·");
	str = str.replaceAll("6", "Êý");
	str = str.replaceAll("7", "Ð´");
	str = str.replaceAll("8", "Àõ");
	str = str.replaceAll("9", "Àã");
	str = str.replaceAll("\\+", "ßã");
	str = str.replaceAll("/", "Êä");
	str = str.replaceAll("=", "Âþ");
	return "·ðÔ»£º" + str;
}

function toman(msg, key) {

	str = msg.substring(4);
	str = str.replaceAll("†ª", "e");
	str = str.replaceAll("ôÉ", "E");
	str = str.replaceAll("ÆÅ", "t");
	str = str.replaceAll("Ìá", "T");
	str = str.replaceAll("Ä¦", "a");
	str = str.replaceAll("ˆÊ", "A");
	str = str.replaceAll("Ú­", "o");
	str = str.replaceAll("åÈ", "O");
	str = str.replaceAll("Ò®", "i");
	str = str.replaceAll("¼ª", "I");
	str = str.replaceAll("æ¶", "n");
	str = str.replaceAll("·ð", "N");
	str = str.replaceAll("Ò¹", "s");
	str = str.replaceAll("ÍÔ", "S");
	str = str.replaceAll("ÄÇ", "h");
	str = str.replaceAll("½÷", "H");
	str = str.replaceAll("Ï¤", "r");
	str = str.replaceAll("Ü¯", "R");
	str = str.replaceAll("°¢", "d");
	str = str.replaceAll("ºô", "D");
	str = str.replaceAll("Èø", "l");
	str = str.replaceAll("Äá", "L");
	str = str.replaceAll("ÍÓ", "c");
	str = str.replaceAll("††", "C");
	str = str.replaceAll("†o", "u");
	str = str.replaceAll("ÒÁ", "U");
	str = str.replaceAll("Â¬", "m");
	str = str.replaceAll("ºÈ", "M");
	str = str.replaceAll("µÛ", "w");
	str = str.replaceAll("Ë¸", "W");
	str = str.replaceAll("õµ", "f");
	str = str.replaceAll("ÃÉ", "F");
	str = str.replaceAll("·£", "g");
	str = str.replaceAll("É³", "G");
	str = str.replaceAll("‡´", "y");
	str = str.replaceAll("Ëû", "Y");
	str = str.replaceAll("ÄÏ", "p");
	str = str.replaceAll("¶¹", "P");
	str = str.replaceAll("ÎÞ", "b");
	str = str.replaceAll("ÔÐ", "B");
	str = str.replaceAll("ÆÐ", "v");
	str = str.replaceAll("Ù¤", "V");
	str = str.replaceAll("âò", "k");
	str = str.replaceAll("¾ã", "K");
	str = str.replaceAll("¶ß", "j");
	str = str.replaceAll("¶È", "J");
	str = str.replaceAll("ð«", "x");
	str = str.replaceAll("ê^", "X");
	str = str.replaceAll("ÊÒ", "q");
	str = str.replaceAll("µØ", "Q");
	str = str.replaceAll("Àû", "z");
	str = str.replaceAll("ÕÚ", "Z");
	str = str.replaceAll("ÄÂ", "0");
	str = str.replaceAll("²Î", "1");
	str = str.replaceAll("Éá", "2");
	str = str.replaceAll("ËÕ", "3");
	str = str.replaceAll("²§", "4");
	str = str.replaceAll("Ò·", "5");
	str = str.replaceAll("Êý", "6");
	str = str.replaceAll("Ð´", "7");
	str = str.replaceAll("Àõ", "8");
	str = str.replaceAll("Àã", "9");
	str = str.replaceAll("ßã", "+");
	str = str.replaceAll("Êä", "/");
	str = str.replaceAll("Âþ", "=");
	return CryptoJS.AES.decrypt("U2FsdGVkX1" + str, key).toString(CryptoJS.enc.Utf8);
}

