import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by chenliang on 14-6-30.
 */
public class Main {

  public static void main(String[] args) throws Exception{
    Workbook workbook = new HSSFWorkbook();

    String[] TAB_NAMES = {"学习时间", "正确率统计", "不会做统计", "没做对统计"};
    String[] DATA_FILES = {"./学习时间统计", "./准确率统", "./不会做统计", "./做错统计"};

    for (int i=0; i < TAB_NAMES.length; i++) {
      Sheet sheet = workbook.createSheet(TAB_NAMES[i]);
      writeToExcel(sheet, parse(DATA_FILES[i]));
    }


    FileOutputStream fileOutputStream = new FileOutputStream("workbook.xls");
    workbook.write(fileOutputStream);

    fileOutputStream.flush();
    fileOutputStream.close();
  }

  private static List<List<String>> parse(String file) throws Exception{
    List<List<String>> data = new ArrayList<List<String>>();

    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(new FileInputStream(file), "UTF-8"));
    String line = null;
    while((line = bufferedReader.readLine()) != null) {
      String[] records = line.split("\t");
      if (records != null) {
        List<String> lineData = new ArrayList<String>();

        for (String record : records) {
          lineData.add(record);
        }

        data.add(lineData);
      }
    }

    return data;
  }

  private static void writeToExcel(Sheet sheet, List<List<String>> data) {
    int rowCount = 0;
    for (List<String> lineData : data) {
      Row row = sheet.createRow(rowCount++);
      int colCount = 0;
      for(String record : lineData) {
        Cell cell = row.createCell(colCount++);
        cell.setCellValue(record);
      }
    }
  }
}
